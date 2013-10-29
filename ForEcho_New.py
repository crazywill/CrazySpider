#!/usr/bin/env python

import os
import sys
from Tools import *
from XmlParse import *
from FormatExcel import *




if __name__=='__main__':
    pwd=os.getcwd()
    pathList=[]
    pathList.append(pwd)
    xmlParse=XmlParse(pwd+'/config.xml')
    fileList=getFileList(pathList,('.xls','xlsx'))
    #print fileList
    #print pwd+'/config.xml'
    #print xmlParse.getInputList()
    #print xmlParse.getOutputList()
    #print xmlParse.getSortList()
    formatExcel=FormatExcel(fileList,xmlParse)
    formatExcel.formatExcel()
