#! /usr/bin/env python

import os
import sys

from Tools import *


if __name__=='__main__':
    args=sys.argv
    if(len(args)<2):
        print 'invalid args'
        exit()
    print args[1]
    pathList=[]
    pathList.append(args[1])
    fileList=getFileList(pathList,('.h','.cpp','.c'))
    for item in fileList:
        path,fileName=os.path.split(item)
        if(fileName[5]!='I'):
            tfileName=fileName[:5]+'I'+fileName[5:]
            tfile=path+'/'+tfileName
            print fileName+'------>'+tfileName
            cmd='mv '+item+' '+tfile
            os.system(cmd)
