#!/usr/bin/env python
import socket
import sys
import os
import time
from twisted.application import internet,service
from twisted.internet import protocol
from twisted.python import log


UDP_PORT = 43278; CHECK_PERIOD = 20; CHECK_TIMEOUT = 15

class Receiver(protocol.DatagramProtocol):
    def datagramReceived(self,data,(ip,port)):
        if data == 'PyHB':
            self.callback(ip)

class DetectorService(internet.TimerService):
    def __init__(self):
        internet.TimerService.__init__(self,CHECK_PERIOD,self.detect)
        self.beats = {}
    def update(self,ip):
        self.beats[ip] = time.time()
    def detect(self):
        limit = time.time()-CHECK_TIMEOUT
        silent = [ip for (ip,ipTime) in self.beats.items() if ipTime<limit]
        log.msg('Silent clients: %s'%silent)

application = service.Application('Heartbeat')
detectorSvc = DetectorService()
detectorSvc.setServiceParent(application)
receiver = Receiver()
receiver.callback = detectorSvc.update
udpServer = internet.UDPServer(UDP_PORT, receiver)
udpServer.setServiceParent(application)
log.msg('Asynchronous heartbeat server listening on port %d\n press Ctrl-c to stop\n'% UDP_PORT)


#address = ("",32000)
#s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(address)

#while True:
#    data,addr=s.recvfrom(2048)
#    if not data:
#        print "client has exit"
#        break
#    print "received:",data,"from",addr

#s.close()
