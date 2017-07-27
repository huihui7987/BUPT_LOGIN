#!/usr/bin/env python
# coding=utf-8
import urllib2

def logout():
    posturl="http://10.3.8.211/F.html"
    header={"User-Agent":"Mozilla/5.0 (compile;MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Referer":"http://10.3.8.211/F.html"
        }
    req = urllib2.Request(posturl,headers=header)
    try:
        response = urllib2.urlopen(req)
	print("Logout success")
    except urllib2.URLError as e:
	print("Logout failed")

if __name__ == '__main__':
    logout()
