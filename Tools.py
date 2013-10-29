#!/usr/bin/env python
# -*- coding=UTF8 -*-
import os
import sys


def getFileList(pathList,postfix):
    fileList=[]
    while len(pathList) > 0:
        path = pathList.pop()
        if os.path.isdir(path):
            result=os.listdir(path)
            for item in result:
                if os.path.isdir(path.rstrip('/')+'/'+item):
                    pathList.append(path.rstrip('/')+'/'+item)
                elif os.path.splitext(item)[1] in postfix and os.path.splitext(item)[1]!="":
                    fileList.append(path.rstrip('/')+'/'+item)
    return fileList


def isDigitType(data):
    return isinstance(data,int) or isinstance(data,float) or isinstance(data,long)




