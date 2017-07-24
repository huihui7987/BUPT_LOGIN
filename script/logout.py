#!/usr/bin/python

import urllib2
import urllib
import requests
import json

def logout():
    posturl="http://10.3.8.211/F.html"
    header={"User-Agent":"Mozilla/5.0 (compile;MSIE 10.0; Windows NT 6.1; Trident/6.0)",
	"Referer":"http://10.3.8.211/F.html"
        }
    response = requests.request('GET',url=posturl, headers=header)
    if response.status_code == 200:
	print("Logout success")
    else:
	print("Logout failed")

if __name__ == '__main__':
    logout()
