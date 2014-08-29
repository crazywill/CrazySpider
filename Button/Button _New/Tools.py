#!/usr/bin/env python
# -*- coding=UTF8 -*-
import os
import sys
from PIL import Image
import struct

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

def createData(inpath, outpath):
    output=open(outpath,'w')
    im=Image.open(inpath)
    x,y = im.size
    im2=im.convert("RGBA")
    imList=list(im2.getdata())
    output.write(struct.pack('I', x))                # width     | 4         |width of this img
    output.write(struct.pack('I', y))                # height    | 4         |height of this img
    for color in imList:
        output.write(struct.pack('B', color[2]*color[3]/255))
        output.write(struct.pack('B', color[1]*color[3]/255))
        output.write(struct.pack('B', color[0]*color[3]/255))
        output.write(struct.pack('B', color[3]))
    #im.close()
    output.close()
    os.remove(inpath)
