#!/usr/bin/env python
# -*- coding=UTF8 -*-
import xlrd
import xlwt
import os
import sys

def getAllFiles(pathList,fileList,postfix):            
    while len(pathList) > 0:                         
        path=pathList.pop()                          
        if os.path.isdir(path)==True:                          
            result=os.listdir(path)                          
            for item in result:                          
                if os.path.isdir(path.rstrip('/')+'/'+item):               
                    pathList.append(path.rstrip('/')+'/'+item)             
                else:
                    tmp=item.split('.')
                    if (len(tmp)>1) and (cmp(tmp[len(tmp)-1],postfix)==0):
                        fileList.append(path.rstrip('/')+'/'+item)

def isDigitType(data):
    return isinstance(data,int) or isinstance(data,float) or isinstance(data,long)

def formatExcel(path):
    if len(path)>0:
        excelFile = xlrd.open_workbook(path)
        #print path
        sheets=excelFile.sheets()
        outPut=xlwt.Workbook()
        isSave=False
        for sheet in sheets:
            #print sheet.name
            fileOutput=[]
            rows=sheet.nrows
            cols=sheet.ncols
            #print 'cols is %d'%(cols)
            if cols<12:
                continue
            #print 'start work'
            outPutSheet=outPut.add_sheet(sheet.name)
            isSave=True
            #style
            style = xlwt.XFStyle()
            styleN = xlwt.XFStyle()
            font = xlwt.Font()
            
            font.name = 'SimSun'    # 指定“宋体”
            font.colour_index = 0x09
            style.font = font
            
            
            borders = xlwt.Borders()
            borders.left = 1
            borders.right = 1
            borders.top = 1
            borders.bottom = 1
            borders.bottom_colour= 0
            style.borders = borders

            alignment = xlwt.Alignment() # Create Alignment
            alignment.horz = xlwt.Alignment.HORZ_RIGHT # May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER, HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED, HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
            alignment.vert = xlwt.Alignment.VERT_CENTER 

            styleBlueBkg = xlwt.easyxf('pattern: pattern solid, fore_colour gray25;')
            styleBlueBkg.borders=borders

            styleBlueBkgR = xlwt.easyxf('pattern: pattern solid, fore_colour gray25;')
            styleBlueBkgR.borders=borders
            styleBlueBkgR.alignment=alignment

            styleCommon = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
            styleCommon.borders=borders

            styleCommonR = xlwt.easyxf('pattern: pattern solid, fore_colour white;')
            styleCommonR.borders=borders
            styleCommonR.alignment=alignment

            styleNormal = xlwt.easyxf('font: bold on; pattern: pattern solid, fore_colour black;')
            styleNormal.borders=borders
            styleNormal.font=font

            outPutSheet.col(0).width=6666
            outPutSheet.col(1).width=6666
            outPutSheet.col(2).width=6666
            outPutSheet.col(3).width=6666
            outPutSheet.col(4).width=6666
            #end
            for i in range(rows):
                value6=sheet.cell_value(i,6)
                value7=sheet.cell_value(i,7)
                value9=sheet.cell_value(i,9)
                value11=sheet.cell_value(i,11)
                #print type(value9)
                #print type(value11)
                tmp='净申购（元）'
                if i==0:
                    outPutSheet.write(i,0,value6,styleNormal)
                    outPutSheet.write(i,1,value7,styleNormal)
                    outPutSheet.write(i,2,value9,styleNormal)
                    outPutSheet.write(i,3,value11,styleNormal)
                    outPutSheet.write(i,4,unicode(tmp, "utf8"),styleNormal)
                else:
                    #print 'value9: %d value11:%d '%(isDigitType(value9),isDigitType(value11))
                    if isDigitType(value9) and isDigitType(value11):
                        fileOutput.append((value6,value7,value9,value11,value9-value11))
                    else:
                        continue
            fileOutput=sorted(fileOutput, key=lambda x: x[4],reverse=True)
            i=1
            Sum2=0
            Sum3=0
            Sum4=0
            for item in fileOutput:
                if(i%2==1):
                    #pattern.pattern_back_colour = 0x37
                    style=styleBlueBkg
                    styleN=styleBlueBkgR
                else:
                    style=styleCommon
                    styleN=styleCommonR
                outPutSheet.write(i,0,item[0],style)
                outPutSheet.write(i,1,item[1],style)
                outPutSheet.write(i,2,format(item[2],',.2f'),styleN)
                outPutSheet.write(i,3,format(item[3],',.2f'),styleN)
                outPutSheet.write(i,4,format(item[4],',.2f'),styleN)
                i=i+1
                Sum2+=item[2]
                Sum3+=item[3]
                Sum4+=item[4]
            if(i%2==1):
                style=styleBlueBkg
                styleN=styleBlueBkgR
            else:
                style=styleCommon
                styleN=styleCommonR
            outPutSheet.write(i,0,unicode('合计',"utf8"),style)
            outPutSheet.write(i,1,unicode('',"utf8"),style)
            outPutSheet.write(i,2,format(Sum2,',.2f'),styleN)
            outPutSheet.write(i,3,format(Sum3,',.2f'),styleN)
            outPutSheet.write(i,4,format(Sum4,',.2f'),styleN)
        if isSave:
            t=u'统计稿.xls'
            #print t
            #t.encode('gbk')
            savePath=unicode(path.split('.')[0],"gbk")
            #print savePath
            savePath=savePath+t
            #print 'savePath is %s'%(savePath)
            outPut.save(savePath)


#print ""
#print ""
#print "              ((`'-\"``\"\"-'`))"
#print "               )   -    -  ( "
#print "              /   (o _ o)   \  "
#print "              \    ( 0 )    / "
#print "              _'-.._'='_..-'_ "
#print "            /`;#'#'#.-.#'#'#;`\ "
#print "            \_))    '#'    ((_/ "
#print "              #.            .# "
#print "              '#.          .#'  "
#print "              / '#.      .#' \ "
#print "             _\  \\'#   ;#'/  /_ "
#print "            (((___) '#' (___)))"

print ""
print "                (()__(()"
print "                /       \\" 
print "               ( /    \\  \\"
print "                \ o o    /"
print "                (_()_)__/ \\"
print "               / _,==.____ \\"
print "              (   |--|      )"
print "              /\_.|__|'-.__/\_"
print "             / (        /     \\" 
print "             \\  \\      (      /"
print "             )  '._____)    /"
print "           (((____.--(((____/"
print ""
print ""
print '-----------This program is designed for Echo!-------------'
print '----------------Author:  Will-----------------------------'
print '----------------Email:   willwanghanyu@gmail.com----------'
print '----------------Version: 1.02-----------------------------'


currentPath=os.getcwd()
pathList=[]
fileList=[]
fileOutput=[]
pathList.append(currentPath)
getAllFiles(pathList,fileList,'xlsx')
pathList.append(currentPath)
getAllFiles(pathList,fileList,'xls')
#print fileList
for item in fileList:
    formatExcel(item)
print '----------------------Complete!---------------------------'
print '---------------Press ENTER key to exit!-------------------'
line=sys.stdin.readline()
#exit(0)
