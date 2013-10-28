#!/usr/bin/env python

import os
import sys

def isDigit(strRes):
    digitSet=('0','1','2','3','4','5','6','7','8','9','.')
    for i in range(len(strRes)):
        if strRes[i] not in digitSet:
            return False
    return True

def compareOpt(a,b):
    dic={'+':1,'-':1,'*':2,'/':2,'(':3,')':3}
    if (a in dic) and (b in dic):
        return dic[a]-dic[b]
    else:
        return -999

def preproExp(expression):
    result=[]
    digitSet=('0','1','2','3','4','5','6','7','8','9','.')
    digitFlag=False
    for i in range(len(expression)):
        if expression[i]==' ':
            continue
        if len(result)==0:
            result.append(expression[i])
        else:
            if expression[i] in digitSet and isDigit(result[len(result)-1]):
                result[len(result)-1]=result[len(result)-1]+expression[i]
            else:
                result.append(expression[i])
    return result

def getRPN(expression):
    result=[]
    stack=[]
    tmp=preproExp(expression)
    print tmp
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
            while len(stack)>0 and  (compareOpt(stack[len(stack)-1],item)>=0) and (stack[len(stack)-1]!='('):
                result.append(stack.pop())
            stack.append(item)
    while len(stack)>0:
        result.append(stack.pop())
    return result



print getRPN(sys.argv[1])
