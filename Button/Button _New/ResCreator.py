#!/usr/bin/env python
# -*- coding=UTF8 -*- 

from Tools import *
from PIL import Image
import os
import sys
import struct

def writeImgDefine(fileList,path):
    output=open(path+'/ImgResDef.h','w')
    output.write('#ifndef IMGRESDEF_H\n#define IMGRESDEF_H\n#include "ResId.h"\n#include "NGSingleton.h"\n')
    for item in fileList:
        fileName=os.path.splitext(os.path.split(item)[1])[0]
        #print fileName
        output.write('#define IMGID_'+fileName.upper()+' (NGSingleton<ImgResDef>::instOrCreate().'+fileName+')\n')
    output.write('#define IMGID_INVALID (NGSingleton<ImgResDef>::instOrCreate().invalid)\n')
    output.write('class ImgResDef\n{\npublic:\n')
    for item in fileList:
        fileName=os.path.splitext(os.path.split(item)[1])[0]
        output.write('    const imgResId '+fileName+';\n')
    output.write('    const imgResId invalid;\n')
    output.write('private:\n    friend class NGSingleton<ImgResDef>;\n    ImgResDef()\n')
    i=0
    for item in fileList:
        fileName=os.path.splitext(os.path.split(item)[1])[0]
        if i == 0:
            output.write('        :'+fileName+'(\"'+fileName+'\")\n')
        else:
            output.write('        ,'+fileName+'(\"'+fileName+'\")\n')
        i=i+1
    output.write('        ,invalid("")\n')
    output.write('    {}\n};\n#endif //IMGRESDEF_H\n')
    output.close()


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
        x,y = im.size
        #print "width: ",x
        #print "Height: ",y
        im2=im.convert("RGBA")
        imList=list(im2.getdata())
       # print os.path.splitext(item)[0]
        output.write(struct.pack('I', x))                # width     | 4         |width of this img
        output.write(struct.pack('I', y))                # height    | 4         |height of this img
        for color in imList:
            output.write(struct.pack('B', color[2]*color[3]/255))
            output.write( struct.pack('B', color[1]*color[3]/255) )
            output.write( struct.pack('B', color[0]*color[3]/255) )
            output.write( struct.pack('B', color[3]) )
            #print '(',color[2]*color[3]/255,color[1]*color[3]/255,color[0]*color[3]/255,color[3],')'
        output.close()
    writeImgDefine(fileList,pwd)
