#!/usr/bin/env python
import socket
import os
import sys

address = ('localhost',32000)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    msg = raw_input()
    if not msg:
        s.sendto('',address)
        break
    s.sendto(msg,address)

s.close()
