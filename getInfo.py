#!/usr/bin/python
#! coding:utf-8

import urllib2
import json

def getInfo():
        loanListUrlPrefix = 'http://www.renrendai.com/lend/loanList!json.action?pageIndex='
        transferListUrlPreFix = 'http://www.renrendai.com/transfer/transferList!json.action?pageIndex='
        
        usefulInfo = []
        
        for pageIndex in range(3):
                webContent = urllib2.urlopen(loanListUrlPrefix+str(pageIndex+1)).read()
                if webContent[0] == '<':
                        return -1;
                jsonString = json.loads(webContent)
                for element in jsonString["data"]["loans"]:
                        element['isTransfer']=False;
                        element['interest'] = float(element['interest'])
                usefulInfo.extend(jsonString["data"]["loans"])
                if jsonString["data"]["loans"][19]["finishedRatio"] == 100:
                        break;
        
        for pageIndex in range(3):
                webContent = urllib2.urlopen(transferListUrlPreFix+str(pageIndex+1)).read()
                if webContent[0] == '<':
                        return -1;
                jsonString = json.loads(webContent)
                for element in jsonString["data"]["transferList"]:
                        element['isTransfer']=True;
                        element['interest'] = float(element['interest'])
                usefulInfo.extend(jsonString["data"]["transferList"])
                if jsonString["data"]["transferList"][19]["share"] == '0':
                        break;
        
        for elem in reversed(range(len(usefulInfo))):
                if usefulInfo[elem]['isTransfer']==True and usefulInfo[elem]['share']=='0':
                        del usefulInfo[elem]
                        continue
                if usefulInfo[elem]['isTransfer']==False and usefulInfo[elem]['finishedRatio']==100:
                        del usefulInfo[elem]    
        
        
        usefulInfo.sort( key=lambda elemUsefulInfo : elemUsefulInfo["interest"], reverse=True)
        
        return usefulInfo