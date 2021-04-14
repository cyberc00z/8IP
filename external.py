"""
import requests
import re


def getMyExtIp():
    try:
        res = requests.get("http://whatismyip.org")
        myIp = re.compile('(\d{1,3}\.){3}\d{1,3}').search(res.text).group()
        if myIp != "":
            return print(myIp)
    except:
        pass
    return "n/a"

getMyExtIp()
"""
from requests import get 
ip = get('https://ipapi.co/ip/').text
print(ip)