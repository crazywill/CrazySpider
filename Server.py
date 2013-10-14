#!/usr/bin/env python
import socket
import sys
import os

address = ("",32000)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(address)

while True:
    data,addr=s.recvfrom(2048)
    if not data:
        print "client has exit"
        break
    print "received:",data,"from",addr

s.close()
