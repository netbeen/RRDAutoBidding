#!/usr/bin/python
#! coding:utf-8

import urllib2
import json
import time

#抓取表单函数
def getInfo():
        #URL前缀
        loanListUrlPrefix = 'http://www.renrendai.com/lend/loanList!json.action?pageIndex='
        transferListUrlPreFix = 'http://www.renrendai.com/transfer/transferList!json.action?pageIndex='
        
        #声明汇总表单
        usefulInfo = []
        
        #抓取散标投资信息
        for pageIndex in range(99):
#                 time1 = time.time()
                try:
                        webContent = urllib2.urlopen(loanListUrlPrefix+str(pageIndex+1)).read()
                except:  
                        return -1
#                 time2 = time.time()
#                 print '抓取散标投资信息时间：'+str(time2 - time1)
                        
                if webContent[0] == '<':
                        return -1
                jsonString = json.loads(webContent)
                for element in jsonString["data"]["loans"]:
                        element['isTransfer']=False;
                        element['interest'] = float(element['interest'])
                usefulInfo.extend(jsonString["data"]["loans"])
                if jsonString["data"]["loans"][len(jsonString["data"]["loans"])-1]["finishedRatio"] == 100:
                        break
        
        #抓取债券转让信息
        for pageIndex in range(99):
#                 time1 = time.time()
                try:
                        webContent = urllib2.urlopen(transferListUrlPreFix+str(pageIndex+1)).read()
                except:  
                        return -1
#                 time2 = time.time()
#                 print '抓取债权转让信息时间：'+str(time2 - time1)
                
                if webContent[0] == '<':
                        return -1
                jsonString = json.loads(webContent)
                if not jsonString["data"].has_key('transferList'):
                        break
                
                for element in jsonString["data"]["transferList"]:
                        element['isTransfer']=True;
                        element['interest'] = float(element['interest'])
                usefulInfo.extend(jsonString["data"]["transferList"])
                if jsonString["data"]["transferList"][len(jsonString["data"]["transferList"])-1]["share"] == '0':
                        break
#                 else:
#                         print '当前页最后债权转让份数'+str(jsonString["data"]["transferList"][len(jsonString["data"]["transferList"])-1]["share"])
        
        #去除无效信息
        for elem in reversed(range(len(usefulInfo))):
                if usefulInfo[elem]['isTransfer']==True and usefulInfo[elem]['share']=='0':
                        del usefulInfo[elem]
                        continue
                if usefulInfo[elem]['isTransfer']==False and usefulInfo[elem]['finishedRatio']==100:
                        del usefulInfo[elem]    
        
        #按照利率进行排序
        usefulInfo.sort( key=lambda elemUsefulInfo : elemUsefulInfo["interest"], reverse=True)
        
        return usefulInfo