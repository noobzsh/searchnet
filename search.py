#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'shenhzha'
'''
'''
from bs4 import BeautifulSoup
import sys
import re
import urllib2
import urllib
import cookielib
import json
import logging
import csv

csv.field_size_limit(sys.maxint)

csv_result = csv.writer(open('countownandusr.csv','wb'))
csv_error = csv.writer(open('error.csv','wb'))



logging.basicConfig(level=logging.DEBUG)
reload(sys)
sys.setdefaultencoding("utf8")


class CiscoSearch(object):

    def _getHeaders(self):
        headers = {}
        headers['User-Agent']='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
        headers['Authorization']='Basic YXJ0bWFpbGVyLmdlbjphcnRtYWlsZXI='
        #headers['Host']='www.dakele.com'
        headers['Connection']='keep-alive'
        headers['Cache-Control']='max-age=0'
        headers['Accept-Language']='zh-CN,zh;q=0.8'
        headers['Accept-Encoding']='gzip, deflate, br'
        headers['Accept']='text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        return headers

    def login(self,groupname):
        result=[]
        error=[]
        ownlist=[]
        usrlist=[]
        status_code = 0
        stringurl='https://ews-aln-core.cisco.com/itsm/mailer/rest/list/'+groupname
        #testurl='http://blog.csdn.net/cqcre232'
        #req = urllib2.Request(testurl, headers=self._getHeaders())
        req = urllib2.Request(stringurl, headers=self._getHeaders())
        try:
            response = urllib2.urlopen(req)
            #status_code=response.code
            #if (status_code==200):
            #self.operate = self.opener.open(req)
            thePage = response.read()
            #if (status_code != 200):
            #print(status_code)
            #print(groupname)
            #csv_error.writerow(groupname)
            soup = BeautifulSoup(thePage,'html.parser', from_encoding = 'utf-8')
            for own in soup.find_all("div", attrs={"title": re.compile(r"Owner:(\s\w+)?")}):
                #print(own.getText())
                ownlist.append(own.getText())
            #print("ok")
            for usr in soup.find_all("div", attrs={"title": re.compile(r"Member:(\s\w+)?")}):
                #print(usr.getText())
                usrlist.append(usr.getText())
            result.append(groupname)
            result.append(ownlist)
            result.append(usrlist)
            csv_result.writerow(result)
        except urllib2.HTTPError,e:
            #print(status_code)
            error.append(groupname)
            csv_error.writerow(error)
        except urllib2.URLError,e:
            error.append(groupname)
            csv_error.writerow(error)
        except:
            error.append(groupname)
            csv_error.writerow(error)

        


if __name__ == '__main__':
    userlogin = CiscoSearch()
    userlogin.login('onramp_mdm_prod_americas_mdmro')
    sys.stdin.readline()
    csv_reader = csv.DictReader(open('mailergroupresmap.csv','rU'))   
    for row in csv_reader:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin.login(stringname)
        #print(stringname)
        #sys.stdin.readline()
    print("ok")