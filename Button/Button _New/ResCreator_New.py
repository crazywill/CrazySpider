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
    for path in fileList:
        outpath = os.path.splitext(path)[0]+'.dat'
        #print outpath
        createData(path,outpath)
