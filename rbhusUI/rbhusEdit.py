#!/usr/bin/python
from PyQt4 import QtCore, QtGui
import glob
import os
import sys
import datetime

progPath =  sys.argv[0].split(os.sep)
print progPath
if(len(progPath) > 1):
  pwd = os.sep.join(progPath[0:-1])
  cwd = os.path.abspath(pwd)
else:
  cwd = os.path.abspath(os.getcwd())
  
sys.path.append(cwd.rstrip(os.sep) + os.sep + "lib")
import rbhusEditMod
print(cwd.rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep) + os.sep +"rbhus")
sys.path.append(cwd.rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep) + os.sep +"rbhus")
import db
import constants
import utils as rUtils


try:
  _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
  _fromUtf8 = lambda s: s
  

class Ui_Form(rbhusEditMod.Ui_rbhusEdit):
    
    
  def setupUi(self, Form):
    
    self.task = rUtils.tasks(tId = sys.argv[1].rstrip().lstrip())
    self.taskValues = self.task.taskDetails
    
    icon = QtGui.QIcon()
    icon.addPixmap(QtGui.QPixmap(_fromUtf8(cwd.rstrip(os.sep).rstrip("rbhusUI").rstrip(os.sep)+ os.sep +"etc/icons/rbhus.svg")), QtGui.QIcon.Normal, QtGui.QIcon.On)
    Form.setWindowIcon(icon)
    
    rbhusEditMod.Ui_rbhusEdit.setupUi(self,Form)
    self.popEditItems()
    
    self.pushFileName.clicked.connect(self.selectFileName)
    self.pushOutPutDir.clicked.connect(self.selectOutPutDir)
    self.pushBfc.clicked.connect(self.selectBfc)
    self.pushAfc.clicked.connect(self.selectAfc)
    self.pushLogOpen.clicked.connect(self.selectLogBase)
    self.checkAfterTime.clicked.connect(self.afterTimeEnable)
    self.spinRerunThresh.valueChanged.connect(self.getSpinRerunThresh)
    self.spinPriority.valueChanged.connect(self.getPriority)
    self.spinMinBatch.valueChanged.connect(self.getMinBatch)
    self.spinMaxBatch.valueChanged.connect(self.getMaxBatch)
    self.afterTimeEdit.dateTimeChanged.connect(self.afePrint)
    self.comboHostGroup.currentIndexChanged.connect(self.hostGroupPrint)
    self.comboBatching.currentIndexChanged.connect(self.batchStatus)
    self.comboType.currentIndexChanged.connect(self.fileTypePrint)
    self.pushApply.clicked.connect(self.applyNew)
    self.pushCancel.clicked.connect(self.popEditItems)
    self.lineEditAfc.textChanged.connect(self.reset_afc)
    self.lineEditBfc.textChanged.connect(self.reset_bfc)
    self.lineEditFileName.textChanged.connect(self.reset_fileName)
    self.lineEditFrange.textChanged.connect(self.reset_fRange)
    self.lineEditImageName.textChanged.connect(self.reset_imageName)
    self.lineEditLogbase.textChanged.connect(self.reset_logbase)
    self.lineEditOutPutDir.textChanged.connect(self.reset_outPutDir)
    self.lineEditDescription.textChanged.connect(self.reset_desc)
    
    print self.afterTimeEdit.dateTime().toString()
    
    
    self.db_filetype = 0
    self.db_hostgroup = 0
    self.db_filename = 0
    self.db_imagename = 0
    self.db_outputdir = 0
    self.db_bfc = 0
    self.db_afc = 0
    self.db_logbase = 0
    self.db_aftertime = 0
    self.db_rerunthresh = 0
    self.db_priority = 0
    self.db_framerange = 0
    self.db_minbatch = 0
    self.db_maxbatch = 0
    self.db_batch = 0
    self.db_desc = 0
    
  def reset_variables(self):
    self.db_filetype = 0
    self.db_hostgroup = 0
    self.db_filename = 0
    self.db_imagename = 0
    self.db_outputdir = 0
    self.db_bfc = 0
    self.db_afc = 0
    self.db_logbase = 0
    self.db_aftertime = 0
    self.db_rerunthresh = 0
    self.db_priority = 0
    self.db_framerange = 0
    self.db_minbatch = 0
    self.db_maxbatch = 0
    self.db_batch = 0
    self.db_desc = 0
    
    
  def reset_outPutDir(self):
    self.db_outputdir = 1
  
  def reset_logbase(self):
    self.db_logbase = 1
  
  def reset_imageName(self):
    self.db_imagename = 1
  
  def reset_fRange(self):
    self.db_framerange = 1
  
  def reset_fileName(self):
    self.db_filename = 1
  
  def reset_bfc(self):
    self.db_bfc = 1
    
    
  def reset_desc(self):
    self.db_desc = 1
    
  def reset_afc(self):
    self.db_afc = 1
    
    
  def applyNew(self):
    editDict = {}
    if(self.db_filetype):
      editDict["fileType"] = str(self.comboType.currentText())
      self.db_filetype = 0
    if(self.db_hostgroup):
      editDict["hostGroups"] = str(self.comboHostGroup.currentText())
      self.db_hostgroup = 0
    if(self.db_filename):
      editDict["fileName"] = str(self.lineEditFileName.text())
      self.db_filename = 0
    if(self.db_imagename):
      editDict["outName"] = str(self.lineEditImageName.text())
      self.db_imagename = 0
    if(self.db_outputdir):
      editDict["outDir"] = str(self.lineEditOutPutDir.text())
      self.db_outputdir = 0
    if(self.db_bfc):
      editDict["beforeFrameCmd"] = str(self.lineEditBfc.text())
      self.db_bfc = 0
    if(self.db_afc):
      editDict["afterFrameCmd"] = str(self.lineEditAfc.text())
      self.db_afc = 0
    if(self.db_logbase):
      editDict["logBase"] = str(self.lineEditLogbase.text())
      self.db_logbase = 0
    if(self.db_aftertime):
      editDict["afterTime"] = str(self.afterTimeEdit.dateTime().date().year()) +"-"+ str(self.afterTimeEdit.dateTime().date().month()) +"-"+ str(self.afterTimeEdit.dateTime().date().day()) +" "+ str(self.afterTimeEdit.dateTime().time().hour()) +":"+ str(self.afterTimeEdit.dateTime().time().minute()) +":" + str(self.afterTimeEdit.dateTime().time().second())
    if(self.db_rerunthresh):
      editDict["rerunThresh"] = str(self.db_rerunthresh)
      self.db_rerunthresh = 0
    if(self.db_framerange):
      editDict["fRange"] = str(self.lineEditFrange.text())
      self.db_framerange = 0
    if(self.db_priority):
      editDict["priority"] = str(self.db_priority)
      self.db_priority = 0
    if(self.db_batch):
      editDict['batch'] = str(self.db_batch)
    if(self.db_maxbatch):
      editDict['maxBatch'] = str(self.db_maxbatch)
    if(self.db_minbatch):
      editDict['minBatch'] = str(self.db_minbatch)
    if(self.db_desc):
      editDict['description'] = str(self.db_desc)
    print(str(editDict))
    try:
      self.task.edit(editDict)
    except:
      print(str(sys.exc_info()))
      
    self.taskValues = self.task.taskDetails
    self.popEditItems()  
    
  
  def hostGroupPrint(self):
    print(self.comboHostGroup.currentText())
    self.db_hostgroup = 1
    
    
  def fileTypePrint(self):
    print(self.comboType.currentText())
    self.db_filetype = 1
    
  def batchStatus(self):
    print(self.comboBatching.currentText())
    self.db_batch = constants.batchStatus[str(self.comboBatching.currentText())]
    
    
  def afePrint(self):
    print(self.afterTimeEdit.dateTime().date().month())
    print(self.afterTimeEdit.dateTime().date().day())
    print(self.afterTimeEdit.dateTime().date().year())
    print(self.afterTimeEdit.dateTime().time().hour())
    print(self.afterTimeEdit.dateTime().time().minute())
    print(self.afterTimeEdit.dateTime().time().second())
    
  def popEditItems(self):
    if(self.taskValues):
      self.lineEditFileName.setText(self.taskValues['fileName'].replace("\\","/"))
      self.lineEditOutPutDir.setText(self.taskValues['outDir'].replace("\\","/"))
      self.lineEditImageName.setText(self.taskValues['outName'])
      self.lineEditFrange.setText(self.taskValues['fRange'])
      self.lineEditLogbase.setText(self.taskValues['logBase'].replace("\\","/"))
      self.lineEditAfc.setText(self.taskValues['afterFrameCmd'].replace("\\","/"))
      self.lineEditBfc.setText(self.taskValues['beforeFrameCmd'].replace("\\","/"))
      self.spinRerunThresh.setValue(self.taskValues['rerunThresh'])
      self.spinMinBatch.setValue(self.taskValues['minBatch'])
      self.spinMaxBatch.setValue(self.taskValues['maxBatch'])
      self.spinPriority.setValue(self.taskValues['priority'])
      self.afterTimeEdit.setTime(QtCore.QTime(self.taskValues['afterTime'].hour, self.taskValues['afterTime'].minute, self.taskValues['afterTime'].second))
      self.afterTimeEdit.setDate(QtCore.QDate(self.taskValues['afterTime'].year, self.taskValues['afterTime'].month, self.taskValues['afterTime'].day))
      self.lineEditDescription.setText(self.taskValues['description'])
      batchFF = self.taskValues['batch']
      self.comboBatching.setCurrentIndex(batchFF)
      batchAD = constants.batchStatus[batchFF]
      self.setFileTypes()
      self.setHostGroups()
      self.reset_variables()
      return(1)
    else:
      return(0)
  
  
  
  def getSpinRerunThresh(self):
    self.db_rerunthresh = self.spinRerunThresh.value()
    print(self.db_rerunthresh)
    
    
  def getMinBatch(self):
    self.db_minbatch = self.spinMinBatch.value()
    print(self.db_minbatch)

  def getMaxBatch(self):
    self.db_maxbatch = self.spinMaxBatch.value()
    print(self.db_maxbatch)
    
  def getPriority(self):
    self.db_priority = self.spinPriority.value()
    print(self.db_priority)
  
  def afterTimeEnable(self):
    cAT = self.checkAfterTime.isChecked()
    if(cAT):
      self.afterTimeEdit.setEnabled(True)
      self.db_aftertime = 1
    else:
      self.afterTimeEdit.setEnabled(False)

  
  def selectFileName(self):
    fila = QtGui.QFileDialog.getOpenFileName()
    if(fila):
      self.lineEditFileName.setText(fila)
      self.db_filename = fila.replace("\\","/")

  def selectOutPutDir(self):
    fila = QtGui.QFileDialog.getExistingDirectory()
    if(fila):
      self.lineEditOutPutDir.setText(fila.replace("\\","/"))
      self.db_outputdir = fila.replace("\\","/")
      

  def selectLogBase(self):
    fila = QtGui.QFileDialog.getExistingDirectory()
    if(fila):
      self.lineEditLogbase.setText(fila)
      self.db_logbase = fila.replace("\\","/")
  
  def selectBfc(self):
    fila = QtGui.QFileDialog.getOpenFileName()
    if(fila):
      self.lineEditBfc.setText(fila)
      self.db_bfc = fila.replace("\\","/")

  def selectAfc(self):
    fila = QtGui.QFileDialog.getOpenFileName()
    if(fila):
      self.lineEditAfc.setText(fila)
      self.db_afc = fila.replace("\\","/")
      
      
  def setFileTypes(self):
    rows = rUtils.getFileTypes()
    self.comboType.clear()  
    if(rows):
      indx = 0
      setIndx = 0
      for row in rows:
        self.comboType.addItem(_fromUtf8(row))
        print(str(self.taskValues['fileType']))
        if(row.endswith(str(self.taskValues['fileType']))):
          setIndx = indx
        indx = indx + 1
      
      self.comboType.setCurrentIndex(setIndx)
      return(1)
    else:
      return(0)
    

  def setHostGroups(self):
    rows = rUtils.getHostGroups()
    indx = 0
    setIndx = 0  
    self.comboHostGroup.clear()  
    if(rows):
      for row in rows:
        self.comboHostGroup.addItem(_fromUtf8(row))
        if(row.endswith(str(self.taskValues['hostGroups']))):
          setIndx = indx
        indx = indx + 1
        
      self.comboHostGroup.setCurrentIndex(setIndx)
      return(1)
    else:
      return(0)

  
  
  
  def updateTask(self, fieldName, fieldValue):
    try:
      conn = db.connRbhus()
      cursor = conn.cursor()
      cursor.execute("update tasks set "+ fieldName +" = "+ fieldValue +" where id="+ str(sys.argv[1].rstrip().lstrip()))
      cursor.close()
      conn.close()
      print("updated "+ str(fieldName) +" with value "+ str(fieldValue))
    except:
      print("Error connecting to db")
      return(0)
  
    
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  Form = QtGui.QMainWindow()
  ui = Ui_Form()
  ui.setupUi(Form)
  Form.show()
  sys.exit(app.exec_())