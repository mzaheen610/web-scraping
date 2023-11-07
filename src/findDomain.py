"""Accepts a URL, finds and returns the domain name from it"""
import re

def getDomainName(url):
    m = re.search("https?://(www\.)?([^/]+)", url)
    domainName = m.group(2)
    return domainName

def isValidURL(url,domainName):
    if domainName in url:
        return  True
    else:
        return False
    
# print(getDomainName('https://www.google.com/setpref?adwrfafw'))
# print(isValidURL('http://www.google.co.in/services/','google.com'))