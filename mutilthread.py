#coding=utf-8
import threading
from time import ctime,sleep
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

    def login(self,groupname,csv_result,csv_error):
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


def login1():
    userlogin1 = CiscoSearch()
    csv_reader1 = csv.DictReader(open('mailergroupresmap.csv','rU'))   
    csv_result1 = csv.writer(open('countownandusr.csv','wb'))
    csv_error1 = csv.writer(open('error.csv','wb'))
    for row in csv_reader1:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin1.login(stringname,csv_result1,csv_error1)
        #print(stringname)
        #sys.stdin.readline()
    print("1:ok")
        

def login2():
    userlogin2 = CiscoSearch()
    csv_reader2 = csv.DictReader(open('mailergroupresmap2.csv','rU'))   
    csv_result2 = csv.writer(open('countownandusr2.csv','wb'))
    csv_error2 = csv.writer(open('error2.csv','wb'))
    for row in csv_reader2:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin2.login(stringname,csv_result2,csv_error2)
        #print(stringname)
        #sys.stdin.readline()
    print("2:ok")


def login3():
    userlogin3 = CiscoSearch()
    csv_reader3 = csv.DictReader(open('mailergroupresmap3.csv','rU'))
    csv_result3 = csv.writer(open('countownandusr3.csv','wb'))
    csv_error3 = csv.writer(open('error3.csv','wb'))   
    for row in csv_reader3:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin3.login(stringname,csv_result3,csv_error3)
        #print(stringname)
        #sys.stdin.readline()
    print("3:ok")


def login4():
    userlogin4 = CiscoSearch()
    csv_reader4 = csv.DictReader(open('mailergroupresmap4.csv','rU')) 
    csv_result4 = csv.writer(open('countownandusr4.csv','wb'))
    csv_error4 = csv.writer(open('error4.csv','wb'))  
    for row in csv_reader4:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin4.login(stringname,csv_result4,csv_error4)
        #print(stringname)
        #sys.stdin.readline()
    print("4:ok")


def login5():
    userlogin5 = CiscoSearch()
    csv_reader5 = csv.DictReader(open('mailergroupresmap5.csv','rU'))
    csv_result5 = csv.writer(open('countownandusr5.csv','wb'))
    csv_error5 = csv.writer(open('error5.csv','wb'))  
    for row in csv_reader5:
        #print(row)
        stringname=row["GROUP_NAME"]
        userlogin5.login(stringname,csv_result5,csv_error5)
        #print(stringname)
        #sys.stdin.readline()
    print("5:ok")


threads = []
t1 = threading.Thread(target=login1)
threads.append(t1)
t2 = threading.Thread(target=login2)
threads.append(t2)
t3 = threading.Thread(target=login3)
threads.append(t3)
t4 = threading.Thread(target=login4)
threads.append(t4)
t5 = threading.Thread(target=login5)
threads.append(t5)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()
    print("all:ok")