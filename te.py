#!/usr/bin/env python
from twisted.internet import reactor

def gotIP(ip,result):
        result=ip
        reactor.callLater(3, reactor.stop)

result=""
reactor.resolve('example.com').addCallback(gotIP,result)
reactor.run()
print result
