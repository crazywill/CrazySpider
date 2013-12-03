#!/usr/bin/env python
# -*- coding=UTF8 -*- 

from Tools import *
from PIL import Image
import os
import sys
import struct
if __name__=='__main__':
    pwd=os.getcwd()
    pathList=[]
    pathList.append(pwd)
    fileList=getFileList(pathList,('.png'))
    #print fileList
    #print pwd
    for item in fileList:
        output=open(os.path.splitext(item)[0]+'.dat','w')
        im=Image.open(item)
        im2=im.convert("RGBA")
        imList=list(im2.getdata())
        print os.path.splitext(item)[0]
        for color in imList:
            output.write(struct.pack('B', color[2]*color[3]/255))
            output.write( struct.pack('B', color[1]*color[3]/255) )
            output.write( struct.pack('B', color[0]*color[3]/255) )
            output.write( struct.pack('B', color[3]) )
            print '(',color[2]*color[3]/255,color[1]*color[3]/255,color[0]*color[3]/255,color[3],')'
        output.close()
