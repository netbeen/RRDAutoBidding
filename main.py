#!/usr/bin/python
#! coding:utf-8
from getInfo import getInfo
import os
import time

if __name__ == '__main__':
        while True:
                usefulInfo = getInfo();
                if usefulInfo == -1:
                        continue
                i=os.system('clear')
                print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
                print '----------------------------------------------------------------------'
                for element in  usefulInfo[0:10]:
                        if element['isTransfer']==True:
                                print str(element["interest"]) + "\t" + str(element["borrowerLevel"])+ "\t" + str(element["displayLoanType"])+ "\t" + str(element["share"]) + "\t" + "转"
                        else:
                                print str(element["interest"]) + "\t" + str(element["borrowerLevel"])+ "\t" + str(element["displayLoanType"])+ "\t" + str(element["finishedRatio"])
                                 
                 
                
