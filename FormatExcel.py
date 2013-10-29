#!/usr/bin/env python
# -*- coding=UTF8 -*-


import xlwt
import xlrd
import os
import sys
import platform
from XmlParse import *
from Tools import *

class FormatExcel:
    opt=('+','-','*','/')
    def __init__(self,fileList,xmlParse):
        self.fileList=fileList
        self.inputList=xmlParse.getInputList()
        self.outputList=xmlParse.getOutputList()
        self.sortList=xmlParse.getSortList()

    def isValid(self,sheet):
        maxIndex=max(self.inputList, key=lambda x: x.getIndex()).getIndex()
        maxNum=ord(maxIndex)-ord('A')
        return sheet.ncols>=maxNum

    def getAscii(self,x):
        return ord(x)-ord('A')

    def getInputAsciiList(self):
        indexList=[]
        for item in inputList:
            indexList.append(self.getAscii(item.getIndex()))

    def calculateExp(self,RPN,row,rawDataDict):
        result =[]
        for item in RPN:
            if item.isalpha():
                result.append(rawDataDict[item][row])
            elif self.isDigit(item):
                result.append(float(item))
            elif item in FormatExcel.opt:
                b=result.pop()
                a=result.pop()
                if item=='+':
                    c=a+b
                elif item=='-':
                    c=a-b
                elif item=='*':
                    c=a*b
                elif item=='/':
                    c=a/b
                result.append(c)
            else:
                print 'opt error!'
        if len(result) ==1:
            return result[0]
        else:
             print 'there is something wrong in calculating expression!'

    def getRawData(self,sheet):
        rawDataDict={}
        if self.isValid(sheet):
            coln=sheet.ncols
            rown=sheet.nrows
            print 'coln: ',coln
            print 'rown: ',rown
            for item in self.inputList:
                dataList=[]
                for i in range(rown):
                    print 'col',self.getAscii(item.getIndex())
                    dataList.append(sheet.cell_value(i,self.getAscii(item.getIndex())))
                rawDataDict[item.getIndex()]=dataList
        return rawDataDict

    def getOutputData(self,sheet,rown,rawDataDict):
        index=0
        for item in self.outputList:
            sheet.write(0,index,item.getName())
            for i in range(rown):
                if i==0:
                    continue
                else:
                    RPN=self.getRPN(item.getOpt())
                    sheet.write(i,index,self.calculateExp(RPN,i,rawDataDict))
            index+=1

    def formatExcel(self):
        for xmlFile in self.fileList:
            if os.path.isfile(xmlFile):
                excel=xlrd.open_workbook(xmlFile)
                sheets=excel.sheets()
                opExcel=xlwt.Workbook()
                for sheet in sheets:
                    if self.isValid(sheet):
                        rown=sheet.nrows
                        opSheet=opExcel.add_sheet(sheet.name)
                        rawDataDict=self.getRawData(sheet)
                        print 'sheet name: ',sheet.name
                        print 'rawDataDict: ',rawDataDict
                        self.getOutputData(opSheet,rown,rawDataDict)
                opExcel.save(self.getSavePath(xmlFile))

    def getSavePath(self,path):
        systemType=platform.system()
        if cmp(systemType,'Linux')==0:
            path=unicode(os.path.splitext(path)[0],'utf8')+u'统计稿.xls'
        else:
            path=unicode(os.path.splitext(path)[0],'gbk')+u'统计稿.xls'
        return path

    def compareOpt(self,a,b):
        dic={'+':1,'-':1,'*':2,'/':2,'(':3,')':3}
        if (a in dic) and (b in dic):
            return dic[a]-dic[b]
        else:
            return -999

    def isDigit(self,strRes):
        digitSet=('0','1','2','3','4','5','6','7','8','9','.')
        for i in range(len(strRes)):
            if strRes[i] not in digitSet:
                return False
        return True

    def preproExp(self,expression):
        result=[]
        digitSet=('0','1','2','3','4','5','6','7','8','9','.')
        digitFlag=False
        for i in range(len(expression)):
            if expression[i]==' ':
                continue
            if len(result)==0:
                result.append(expression[i])
            else:
                if expression[i] in digitSet and self.isDigit(result[len(result)-1]):
                    result[len(result)-1]=result[len(result)-1]+expression[i]
                else:
                    result.append(expression[i])
        return result


    def getRPN(self,expression):
        result=[]
        stack=[]
        tmp=self.preproExp(expression)
        for item in tmp:
            if item.isalpha() or item.isdigit() :
                result.append(item)
            else:
                if item=='(':
                    stack.append(item)
                    continue
                elif item==')':
                    while len(stack)>0 and stack[len(stack)-1]!='(':
                        result.append(stack.pop())
                    stack.pop()
                    continue
                while len(stack)>0 and  (self.compareOpt(stack[len(stack)-1],item)>=0) and (stack[len(stack)-1]!='('):
                    result.append(stack.pop())
                stack.append(item)
        while len(stack)>0:
            result.append(stack.pop())
        return result



    def setFileList(self,fileList):
        self.fileList=fileList
    
    def getFileList(self):
        return self.fileList

    def setInputList(self,inputList):
        self.inputList=inputList

    def getInputList(self):
        return self.inputList
    
    def setOutputList(self,outputList):
        self.outputList=outputList

    def getOutputList(self):
        return self.outputList

    def setSortList(self,sortList):
        self.sortList=sortList

    def getSortList(self):
        return self.sortList



