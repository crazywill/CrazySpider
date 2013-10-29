#!/usr/bin/env python
# -*- coding=UTF8 -*-

import os
import sys
from xml.dom import minidom
_DEBUG=False
if _DEBUG == True:
    import pdb

class InputConfig:
    def __init__(self,index):
        self.index=index

    def getIndex(self):
        return self.index

    def setIndex(self,index):
        self.index=index

class OutputConfig:
    def __init__(self,name,opt):
        self.name=name
        self.opt=opt

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name

    def setOpt(self,opt):
        self.opt=opt

    def getOpt(self):
        return self.opt

class SortConfig:
    def __init__(self,index,opt):
        self.index=index
        self.opt=opt

    def setIndex(self,index):
        self.index=index

    def getIndex(self):
        return self.index

    def setOpt(self,opt):
        self.opt=opt

    def getOpt(self):
        return self.opt

class XmlParse:
    def __init__(self,path):
        self.path=path
        self.inputList=[]
        self.outputList=[]
        self.sortList=[]
        if _DEBUG == True:
            pdb.set_trace()
        self.parseXml()

    def getInputList(self):
        return self.inputList

    def getOutputList(self):
        return self.outputList

    def getSortList(self):
        return self.sortList

    def getPath(self):
        return self.path

    def setPath(self,path):
        self.path=path

    def parseXml(self):
        print self.path
        print os.path.isfile(self.path)
        print os.path.splitext(self.path)[1] in ('.xml')
        if os.path.isfile(self.path) and os.path.splitext(self.path)[1] in ('.xml'):
            print 'start process'
            doc=minidom.parse(self.path)
            root=doc.documentElement
            #get input
            inputTag=root.getElementsByTagName('input')
            for itElement in inputTag:
                colTag=itElement.getElementsByTagName('col')
                for colElement in colTag:
                    index=colElement.getAttribute('index').upper()
                    inputConfig=InputConfig(index)
                    self.inputList.append(inputConfig)
                    print 'input :',index

            #get output
            outputTag=root.getElementsByTagName('output')
            for otElement in outputTag:
                colTag=otElement.getElementsByTagName('col')
                for colElement in colTag:
                    name=colElement.getAttribute('name')
                    opt=colElement.getAttribute('opt').upper()
                    outputConfig=OutputConfig(name,opt)
                    self.outputList.append(outputConfig)
                    print 'output: ',name,opt
            #get sort
            sortTag=root.getElementsByTagName('sort')
            for stElement in sortTag:
                colTag=stElement.getElementsByTagName('col')
                for colElement in colTag:
                    index=colElement.getAttribute('index').upper()
                    opt=colElement.getAttribute('opt').upper()
                    sortConfig=SortConfig(index,opt)
                    self.sortList.append(sortConfig)
                    print 'sort: ',index,opt
        else:
            print 'xml path is invalid'



