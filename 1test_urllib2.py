# coding:utf-8

import urllib2,cookielib

url = "http://baidu.com"

print "第一种方法"
request1 = urllib2.urlopen(url)
print request1.getcode()

print '第二种方法'
request2 = urllib2.Request(url)
request2.add_header('user-agent','Mozila/5.0')
response2 = urllib2.urlopen(request2)
print response2.getcode()
print len(response2.read())

print '第三种方法'
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(request2)
print response3.getcode()
print cj
print response3.read()

