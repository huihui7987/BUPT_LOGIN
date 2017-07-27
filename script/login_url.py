#!/usr/bin/env python
# coding=utf-8
import urllib2
import urllib
import getpass
def login(username,password):
    posturl="http://10.3.8.211/"
    header={"User-Agent":"Mozilla/5.0 (compile;MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Referer":"http://10.3.8.211/"
        }
    postdata={
	"DDDDD":username, 
	"upass":password,
	"savePWD":"0",
	"0MKKey":""
        }
    postData = urllib.urlencode(postdata)
    req = urllib2.Request(posturl,postData,header)
    try:
        response = urllib2.urlopen(req)
	print("Login sucess")
    except urllib2.URLError as e:
	print("Login Failed") 
if __name__ == '__main__':    
    name = raw_input("please input the username:")
    password = getpass.getpass("Password:")
    name = name.strip()
    login(name,password)
#postData=urllib.urlencode(postdata)
#request=urllib2.Request(posturl,postData,header)
#response=urllib2.urlopen(request)
