#!/usr/bin/env python

from XmlParse import *
from Tools import *
import os
import sys


if __name__=='__main__':
    pathList=[]
    pathList.append('./')
    print getFileList(pathList,('.py'))
    exit(0)
    xmlParse=XmlParse(sys.argv[1])
    xmlParse.parseXml()
    inputList=xmlParse.getInputList()
    outputList=xmlParse.getOutputList()
    sortList=xmlParse.getSortList()

    print 'input'
    for item in inputList:
        print 'index: ',item.getIndex()
    print 'output'
    for item in outputList:
        print 'name: ',item.getName()
        print 'opt: ',item.getOpt()
    print 'sort'
    for item in sortList:
        print 'index: ',item.getIndex()
        print 'opt: ',item.getOpt()
