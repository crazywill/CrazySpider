#!/usr/bin/env python


import xlwt
import xlrd
import os
import sys
from XmlParse import *

class FormatExcel:
    def __init__(self,fileList,inputList,outputList,sortList):
        self.fileList=fileList
        self.inputList=inputList
        self.outputList=outputList
        self.sortList=sortList

    def isValid(self,sheet):
        maxIndex=max(inputList, key=lambda x: x.getIndex()).getIndex()
        maxNum=ord(maxIndex)-ord('A')
        return sheet.ncols<maxNum

    def getAscii(self,x):
        return ord(x)-ord('A')

    def getInputAsciiList(self):
        indexList=[]
        for item in inputList:
            indexList.append(self.getAscii(item.getIndex()))

    def getRawData(self,sheet):
        rawDataDict={}
        if self.isValid(sheet):
            coln=sheet.ncols
            rown=sheet.nrows
            for item in inputList:
                dataList=[]
                for i in range(rown):
                    dataList.append(sheet.cell_value(i,self.getAscii(item.getIndex())))
                rawDataDict[item.getIndex]=dateList
        return rawDataDict

    def getOutputData(self,sheet):
        otDataList=[]
        return otDataList

    def formatExcel(self):
        for xmlFile in fileList:
            if os.path.isfile(xmlFile):
                excel=xlrd.open_workbook(xmlFile)
                sheets=excel.sheets()
                opExcel=xlwt.Workbook()
                for sheet in sheets:
                    if self.isValid(sheet):
                        opSheet=opExcel.add_sheet(sheet.name)

    def setFileList(self,fileList):
        self.fileList=fileList
    
    def getFileList(self):
        return self.fileList

    def setInputList(self,inputList)
        self.inputList=inputList

    def getInputList(self):
        return self.inputList
    
    def setOutputList(self,outputList);
        self.outputList=outputList

    def getOutputList(self):
        return self.outputList

    def setSortList(self,sortList):
        self.sortList=sortList

    def getSortList(self):
        return self.sortList



