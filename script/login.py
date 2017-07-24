import urllib2
import urllib
import requests
import getpass
import json
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
    response = requests.request('POST',url=posturl, data=postdata, headers=header)
    if response.status_code == 200:
	print("Login sucess")
    else:
	print("Login Failed") 
if __name__ == '__main__':    
    name = raw_input("please input the username:")
    password = getpass.getpass("Password:")
    name = name.strip() #去除空格
    login(name,password)
#postData=urllib.urlencode(postdata)
#request=urllib2.Request(posturl,postData,header)
#response=urllib2.urlopen(request)
