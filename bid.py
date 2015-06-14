#!/usr/bin/python
#! coding:utf-8

import urllib2
import urllib
import json
import cookielib

# url = 'http://www.renrendai.com/getUsableCoupon.action?payAmount=50&businessCategory=LOAN&t=1434210900047'
# login_data = urllib.urlencode({'renrendaiUsername': '394062113@qq.com','rrd_key':'Mzk0MDYyMTEzQHFxLmNvbToxNDM0MjEzNTgwNzk0OjY4MWFlNzhhMjc4YzIxZGEyOWRlMmQzMGUxMTI0NWM1OjIxMC43NS4yNTIuMjM2'})  
# 
# cj = cookielib.CookieJar()  
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))  
# urllib2.install_opener(opener)
# #opener.open(url, login_data)
# 
# #print opener
# req = urllib2.Request(url=url,data=login_data)
# webContent = urllib2.urlopen(req).read()
# 
# print webContent

#renrendaiUsername="394062113@qq.com"; expires=Sat, 27 Jun 2015 15:53:51 GMT; path=/; domain=www.renrendai.com
#rrd_key=Mzk0MDYyMTEzQHFxLmNvbToxNDM0MjEzNTgwNzk0OjY4MWFlNzhhMjc4YzIxZGEyOWRlMmQzMGUxMTI0NWM1OjIxMC43NS4yNTIuMjM2; expires=Sat, 13 Jun 2015 16:39:45 GMT; path=/; domain=www.renrendai.com; HttpOnly

cookies = urllib2.HTTPCookieProcessor()
opener = urllib2.build_opener(cookies)
f = opener.open('http://www.xxxx.net/?act=login&name=user01')
data = '<root>Hello</root>'
request = urllib2.Request(
        url     = 'http://www.xxxx.net/?act=send',
        headers = {'Content-Type' : 'text/xml'},
        data    = data)
opener.open(request)