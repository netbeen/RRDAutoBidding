

import urllib2
import json

# loanListUrlPrefix = 'http://www.renrendai.com/lend/loanList!json.action?pageIndex='
# jsonString = json.loads(urllib2.urlopen(loanListUrlPrefix+str('1')).read())
# print jsonString


try:
        url="http://www.renrendai.com/lend/loanList!json.action?pageIndex=1";
        request = urllib2.Request(url)
        request.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.8.1.14) Gecko/20080404 (FoxPlus) Firefox/2.0.0.14')
        response = urllib2.urlopen(request).read()
        print response
except urllib2.HTTPError, e:
        print e.code