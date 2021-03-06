#!/usr/bin/env python2
#-*- coding: utf-8 -*-
__author__ = "Shrinidhi Rao"
__license__ = "GPL"
__email__ = "shrinidhi666@gmail.com"

import zmq
import uuid
import time
import sys
import simplejson

message_str = {"test":"testing",
               "project":"AndePirki_se01_ep003_SavingPrivateRyan",
               "asset":"AndePirki_se01_ep003_SavingPrivateRyan:library:sq01:sc001:anim:rig:blend",
               "run":"review"
               }
message = simplejson.dumps(message_str)
ip = "127.0.0.1"
port = 8989
context = zmq.Context()
request_id = uuid.uuid4()

socket = context.socket(zmq.REQ)
socket.connect("tcp://{0}:{1}".format(ip, port))
socket.poll(timeout=1)
poller = zmq.Poller()
poller.register(socket, zmq.POLLIN)
print ("Sending request {0} …".format(request_id))
# send_msg = self.process(message)
timestarted = time.time()

socket.send_multipart([bytes(request_id),bytes(message)])
while(True):
  sockets = dict(poller.poll(10000))
  if(sockets):
    for s in sockets.keys():
      if(sockets[s] == zmq.POLLIN):
        try:
          (recv_id, recved_msg) = s.recv_multipart()
          # recv_message = self.process(recved_msg)
        except:
          print (sys.exc_info())
        break
    break
  print ("Reciever Timeout error : Check if the server is running")


print ("Received reply %s : %s [ %s ]" % (recv_id,recved_msg, time.time() - timestarted))
socket.close()