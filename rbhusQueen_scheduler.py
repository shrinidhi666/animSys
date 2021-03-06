#!/usr/bin/python
###
# Copyright (C) 2012  Shrinidhi Rao shrinidhi@clickbeetle.in
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
###

# SERVER!!!!!!!!
import sys
import os
import logging
import logging.handlers
import time
import signal
import setproctitle
import tempfile
import uuid
import rbhus.dbRbhus as dbRbhus
import rbhus.constants as constants

LOG_FILENAME = '/var/log/rbhusQueen_scheduler.log'
logging.BASIC_FORMAT = "%(asctime)s - %(funcName)s - %(levelname)s - %(message)s"
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

db_conn = dbRbhus.dbRbhus()
tempDir = tempfile.gettempdir()
mainPidFile = tempDir + os.sep +"rbusServer.pids"





setproctitle.setproctitle("rQ_scheduler")

def getFreeHosts():
  freeHosts = []
  potentHosts = db_conn.getPotentHosts()
  #logging.debug("potentHosts : "+ str(potentHosts))
  if(potentHosts):
    for hostDetails in potentHosts:
      loadThreshold = 0 
      if(hostDetails['os'].find("linux") >= 0):
        loadThreshold = hostDetails["totalCpus"] - 1
      elif(hostDetails['os'].find("win") >= 0):
        loadThreshold = 90
      if(hostDetails["eCpus"] == 0):
        hostDetails["eCpus"] = hostDetails["totalCpus"]
        if((hostDetails["freeCpus"] <= hostDetails["totalCpus"]) and (hostDetails["freeCpus"] > 0)):
          if((100 * float(hostDetails['freeRam']) / float(hostDetails['totalRam'])) >= 10): 
            if(hostDetails['load1'] <= loadThreshold):
              freeHosts.append(hostDetails)
      elif(hostDetails['eCpus'] != 0):
        if((hostDetails["totalCpus"] - hostDetails["freeCpus"]) < hostDetails["eCpus"]):
          if((100 * float(hostDetails['freeRam']) / float(hostDetails['totalRam'])) >= 10): 
            if(hostDetails['load1'] <= loadThreshold):
              freeHosts.append(hostDetails)
  return(freeHosts)

def getBestHost(activeTask,freeHosts):
  #freeHosts = getFreeHosts()
  #logging.debug("free host : "+ str(freeHosts))
  #Try to giv to the last host that the task ran
  print("trying to get a bestHost for "+ str(activeTask['id']))
  for freeHost in freeHosts:
    if(not activeTask['lastHost']):
      activeTask['lastHost'] = ""
    if(freeHost['hostName'].find(activeTask['lastHost']) >= 0):
      hostGroups = freeHost["groups"].split(",")
      taskGroups = activeTask["hostGroups"].split(",")
      hostOss = freeHost["os"].split(",")
      taskOss = activeTask["os"].split(",")
      inOSflag = 1
      for tOs in taskOss:
        if(tOs not in hostOss):
          inOSflag = 0

      inGroupFlag = 1
      for taskGroup in taskGroups:
        if(taskGroup not in hostGroups):
          inGroupFlag = 0

      if(inGroupFlag and inOSflag):
        if(freeHost['freeRam'] >= activeTask['minRam']):
          if(activeTask['threads'] == 0):
            if(freeHost['totalCpus'] - freeHost['freeCpus'] == 0):
              #logging.debug("free host : "+ str(freeHost))
              try:
                freeHosts.remove(freeHost)
              except:
                logging.error("removing freehost "+ str(freeHost['hostName']) +" : "+ str(sys.exc_info()))
              return(freeHost)
            
          else:
            if((freeHost['freeCpus'] - activeTask['threads']) >= (freeHost['totalCpus'] - freeHost['eCpus'])):
              #logging.debug("free host : "+ str(freeHost))
              try:
                freeHosts.remove(freeHost)
              except:
                logging.error("removing freehost "+ str(freeHost['hostName']) +" : "+ str(sys.exc_info()))
              return(freeHost)

  #If no last host then find a new one :)
  for freeHost in freeHosts:
    hostGroups = freeHost["groups"].split(",")
    taskGroups = activeTask["hostGroups"].split(",")
    hostOss = freeHost["os"].split(",")
    taskOss = activeTask["os"].split(",")
    inOSflag = 0
    for tOs in taskOss:
      if(tOs in hostOss):
        inOSflag = 1
        break

    inGroupFlag = 0
    for taskGroup in taskGroups:
      if(taskGroup in hostGroups):
        inGroupFlag = 1
        break
    if(inGroupFlag and inOSflag):
      if(freeHost['freeRam'] >= activeTask['minRam']):
        if(activeTask['threads'] == 0):
          if(freeHost['totalCpus'] - freeHost['freeCpus'] == 0):
            #logging.debug("free host : "+ str(freeHost))
            try:
              freeHosts.remove(freeHost)
            except:
              logging.error("removing freehost "+ str(freeHost['hostName']) +" : "+ str(sys.exc_info()))
            return(freeHost)
        else:
          if((freeHost['freeCpus'] - activeTask['threads']) >= (freeHost['totalCpus'] - freeHost['eCpus'])):
            #logging.debug("free host : "+ str(freeHost))
            try:
              freeHosts.remove(freeHost)
            except:
              logging.error("removing freehost "+ str(freeHost['hostName']) +" : "+ str(sys.exc_info()))
            return(freeHost)
  return(0)

def arrangedActiveTasks():
  priorities = {}
  arrangedTasks = []
  activeTasks = db_conn.getActiveTasks()
  afterTasks = {}
  #logging.debug("activeTasks :"+ str(activeTasks))
  if(activeTasks):
    
    taskRunFrames = {}
    for activeTask in activeTasks:
      trf =  db_conn.getRunFrames(activeTask["id"])
      if(trf):
        taskRunFrames[activeTask["id"]] = len(trf)
      else:
        taskRunFrames[activeTask["id"]] = 0
      
    
    
    #logging.debug("w1")
    for activeTask in activeTasks:
      try:
        priorities[activeTask["priority"]].append(activeTask)
      except:
        priorities[activeTask["priority"]] = []
        priorities[activeTask["priority"]].append(activeTask)

    pKeys = priorities.keys()
    pKeys.sort(reverse=True)
    #logging.debug("Sorted Keys :"+ str(pKeys))

    numPrios = len(pKeys)
    totalPrios = sum(pKeys)

    pcentPkeys = {}
    for pKey in pKeys:
      pcentPkeys[pKey] = (float(pKey) * 100) / float(totalPrios)
    #logging.debug("pcentPkeys :" + str(pcentPkeys))

    pcentPkeysRun = {}
    totalRunFrames = sum([taskRunFrames[x] for x in taskRunFrames])
    for pKey in pKeys:
      runFrames = 0
      for activeTask in priorities[pKey]:
        runShit = taskRunFrames[activeTask["id"]]
        runFrames = runFrames + runShit
      try:
        pcentPkeysRun[pKey] = (100 * float(runFrames)) / float(totalRunFrames)
      except:
        pcentPkeysRun[pKey] = 0
    #logging.debug("pcentPkeysRun :"+ str(pcentPkeysRun))

    #The logic below SUCKS!!!! :`(
    pKeysTmp = pKeys
    pKeysRevised = []
    while(len(pKeysTmp)):
      doneCrapping = 0
      for pKey in pKeysTmp:
        if(pcentPkeysRun[pKey] <= pcentPkeys[pKey]):
          pKeysRevised.append(pKey)
          pKeysTmp.remove(pKey)
          doneCrapping = 1
          break
      if(doneCrapping == 0):
        for pKey in pKeysTmp:
          pKeysRevised.append(pKey)
        break

    #logging.debug("RevisedPkeys : "+ str(pKeysRevised))

    for pKey in pKeysRevised:
      pcent = {}
      for activeTask in priorities[pKey]:
        completedShit = 0
        completedShit = taskRunFrames[activeTask["id"]]
        allFrames = 0
        allFrames = db_conn.getAllFrames(activeTask["id"])
        if(allFrames):
          numAllFrames = len(allFrames)
        else:
          return(0)

        if(completedShit):
          numCompletedShit = completedShit
        else:
          numCompletedShit = 0
        percent = (100 * numCompletedShit) / numAllFrames
        try:
          pcent[percent].append(activeTask)
        except:
          pcent[percent] = []
          pcent[percent].append(activeTask)
      pcentKeys = pcent.keys()
      pcentKeys.sort()
      for pcentKey in pcentKeys:
        tasks = pcent[pcentKey]
        for task in tasks:
          arrangedTasks.append(task)
    #logging.debug("arrangedTasks :"+ str(arrangedTasks))

      
        
    afterTasks = []
    for activeTask in arrangedTasks:
      if(activeTask["afterTasks"]!="0"):
        afts = activeTask["afterTasks"].split(",")
        print(afts)
        for af in afts:
          try:
            if(int(af) in [int(x['id']) for x in arrangedTasks]):
              afterTasks.append(activeTask)
              break
          except:
            break
    if(afterTasks):
      for x in afterTasks:
        try:
          arrangedTasks.remove(x)
        except:
          pass
        if(x['afterTaskSloppy'] == constants.afterTaskSloppyEnable):
          arrangedTasks.append(x)
      
    runFirst = []
    reArrangedTasks = arrangedTasks
    for x in arrangedTasks:
      if(x['fastAssign'] == constants.fastAssignEnable):
        try:
          reArrangedTasks.remove(x)
        except:
          pass
        runFirst.append(x)
    runFirst.reverse()
    for x in runFirst:
      reArrangedTasks.insert(0,x)


    
    return(reArrangedTasks)
  else:
    return(0)

def assignFramesToHost(hostDetail,taskDets, taskFrames, batchId):
  eThreads = 0
  if(taskDets['threads'] == 0):
    if(hostDetail['eCpus'] == 0):
      eThreads = hostDetail['freeCpus']
    else:
      eThreads = hostDetail['freeCpus'] - (hostDetail['totalCpus'] - hostDetail['eCpus'])
  else:
    eThreads = taskDets['threads']

  framesStr = " or frames.frameId=".join(str(x) for x in taskFrames)
  db_conn.execute("UPDATE hostResource \
                  SET freeCpus=freeCpus-"+ str(eThreads) +" \
                  WHERE ip=\""+ hostDetail['ip'] +"\"")
  db_conn.execute("UPDATE frames \
                  SET hostName=\""+ hostDetail['hostName'] +"\" , \
                  status=if(frameId="+ str(min(taskFrames)) +","+ str(constants.framesAssigned) +","+ str(constants.framesBatched) +"), \
                  runCount=runCount+1 , \
                  ip='"+ str(hostDetail['ip']) +"' , \
                  batchId=\""+ str(batchId) +"\", \
                  fThreads="+ str(eThreads) +" \
                  WHERE (frames.frameId="+ framesStr +") \
                  AND frames.id="+ str(taskDets["id"]))
  #db_conn.execute("UPDATE hostResource \
                  #SET freeCpus=freeCpus+"+ str(eThreads) +" \
                  #WHERE hostName=\""+ hostDetail['hostName'] +"\"")
  db_conn.execute("UPDATE tasksLog SET lastHost=\""+ hostDetail['hostName'] +"\" WHERE tasksLog.id="+ str(taskDets['id']))


def assignBatchToHost(hostDetail,taskDets, batchId):
  eThreads = 0
  if(taskDets['threads'] == 0):
    if(hostDetail['eCpus'] == 0):
      eThreads = hostDetail['freeCpus']
    else:
      eThreads = hostDetail['freeCpus'] - (hostDetail['totalCpus'] - hostDetail['eCpus'])
  else:
    eThreads = taskDets['threads']

  db_conn.execute("UPDATE hostResource \
                  SET freeCpus=freeCpus-"+ str(eThreads) +" \
                  WHERE ip=\""+ hostDetail['ip'] +"\"")
  db_conn.execute("UPDATE batch \
                  SET host=\""+ hostDetail['ip'] +"\" , \
                  status="+ str(constants.framesAssigned) +", \
                  fThreads="+ str(eThreads) +" \
                  WHERE batch.id='"+ str(batchId) +"'")
  #db_conn.execute("UPDATE hostResource \
                  #SET freeCpus=freeCpus+"+ str(eThreads) +" \
                  #WHERE hostName=\""+ hostDetail['hostName'] +"\"")
  db_conn.execute("UPDATE tasksLog SET lastHost=\""+ hostDetail['hostName'] +"\" WHERE tasksLog.id="+ str(taskDets['id']))



def initBatchId(taskid):
  try:
    bUid = str(uuid.uuid4())
    db_conn.execute("insert into batch (id, taskId) value ('"+ str(bUid) +"',"+ str(taskid) +")")
  except:
    logging.error("batchId failed : "+ str(sys.exc_info()))
    raise
  return(str(bUid))


def insertFramesInToBatchId(batchId,frameNo):
  try:
    db_conn.execute("update batch set frange=CONCAT(frange,\" "+ str(frameNo) +" \") where id=\""+ str(batchId) +"\"")
    logging.debug("adding frame : "+ str(frameNo) +" to batchId : "+ str(batchId))
  except:
    logging.error("adding frame to batchId failed : "+ str(sys.exc_info()))
    return(0)
  return(1)


def getMinMaxCpus():
  try:
    rows = db_conn.execute("select max(hostInfo.totalCpus),min(hostInfo.totalCpus) from hostInfo,hostAlive where hostInfo.ip= hostAlive.ip and hostAlive.status="+ str(constants.hostAliveAlive),dictionary=True)
    if(rows):
      try:
        return(rows[0])
      except:
        logging.error("min max cpus failed : "+ str(sys.exc_info()))
    return(0)
  except:
    logging.error("min max cpus failed : "+ str(sys.exc_info()))
    return(0)

def scheduler():
  while(1):
    freeHosts = getFreeHosts()
    #logging.debug("f1")
    if(freeHosts):
      #logging.debug("f2")
      activeTasks = arrangedActiveTasks()
      #print("_______________________________________________________________________________________________")
      if(activeTasks):
        assigned = 0
        for activeTask in activeTasks:
          taskFrames = db_conn.getUnassignedFrames(activeTask["id"])
          batchFlag = activeTask["batch"]
          minBatch = activeTask["minBatch"]
          maxBatch = activeTask["maxBatch"]

          if(taskFrames):
            totalFreeHosts = len(freeHosts)
            totalTaskFrames = len(taskFrames)
            assignedHost = getBestHost(activeTask,freeHosts)
            if(assignedHost):
              print("got a bestHost for "+ str(activeTask['id']) +" : "+ str(assignedHost['hostName']))
              #Initialize batch id for the frame
              while(1):
                try:
                  batchId = initBatchId(activeTask['id'])
                  break
                except:
                  time.sleep(1)

              bestBatch = 1
              if(batchFlag == constants.batchActive):
                
                minMaxCpus = getMinMaxCpus()
                maxCpu = int(minMaxCpus['max(hostInfo.totalCpus)'])
                minCpu = int(minMaxCpus['min(hostInfo.totalCpus)'])
                cpuRange = maxCpu - minCpu
                batchRange = maxBatch - minBatch
                bestBatch = (((int(assignedHost['totalCpus']) - minCpu)*batchRange)/cpuRange) + minBatch
                
                if(bestBatch < minBatch):
                  bestBatch = minBatch
                if(bestBatch > maxBatch):
                  bestBatch = maxBatch
                if(bestBatch > totalTaskFrames):
                  bestBatch = totalTaskFrames
              taskFramesToAssign = []
              print("bestBatch : "+ str(bestBatch) +" : "+ str(assignedHost['hostName']) +" : "+ str(assignedHost['totalCpus']) +" : "+ str(activeTask['id']))
              for bB in range(0,bestBatch):
                print("batch id : " + str(batchId) +" : "+ str(taskFrames[bB]['frameId']))
                insertFramesInToBatchId(batchId,taskFrames[bB]['frameId'])
                taskFramesToAssign.append(taskFrames[bB]['frameId'])
              #assignBatchToHost(assignedHost, activeTask, batchId)  
              assignFramesToHost(assignedHost, activeTask, taskFramesToAssign, batchId)
              logging.debug("batchID : "+ str(batchId) +" : ASSIGNED to "+ assignedHost["hostName"] +" : "+ str(activeTask["id"]) +" : "+ str(taskFramesToAssign))
              assigned = 1
              break
            print("no bestHost for "+ str(activeTask['id']))
          else:
            while(1):
              if(db_conn.resetFailedFrames(activeTask["id"])):
                break
              time.sleep(1)
              
            #check if task is done . 
            while(1):
              if(db_conn.setTaskDone(activeTask["id"])):
                break
              time.sleep(1)
    else:
      time.sleep(0.5)
    time.sleep(0.2)






if __name__=="__main__":
  import traceback
  while(True):
    try:
      scheduler()
    except:
      traceback.print_exc()
    time.sleep(2)


