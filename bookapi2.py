# setting 수정
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SCLproject.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# ------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
from booksearch.models import Book
import time
import xmltodict
import json

"""
libName: 소장도서관(이름)
callNo: 청구기호
title: 제목
author: 저작자
publisher: 발행자(출판사)
pubYear: 발행년도
isbn: 낱권ISBN
"""

open_url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi?serviceKey=0OhBU7ZCGIobDVKDeBJDpmDRqK3IRNF6jlf%2FJB2diFAf%2FfR2czYO9A4UTGcsOwppV6W2HVUeho%2FFPwXoL6DwqA%3D%3D'
code = ['MA','MB','MC','MD','ME','MF','MG','MH','MV','MJ','MK'
        ,'ML','MX','MM','MP','MW','MN','MQ','MR','MS','MT','MU']

# 함수 -------------------------------------------------------
dic = ['libName', 'callNo', 'title', 'author', 'publisher', 'pubYear', 'isbn']
def book(code):

    for page in range(1,2):
        url = open_url + f'&title=&manageCd={code}&numOfRows=50&pageNo=' + str(page)
        res = requests.get(url)
        xpars = xmltodict.parse(res.text)
        jsonDump = json.dumps(xpars)
        jsonBody = json.loads(jsonDump)
        data = jsonBody['response']['body']['items']['item']
        for i in data:
            try:
                Book(libname=i['libName'],
                     callno=i['callNo'],
                     title=i['title'],
                     author=i['author'],
                     publisher=i['publisher'],
                     pubyear=i['pubYear'],
                     isbn=i['isbn']).save()
            except KeyError:
                Book(libname=None,
                     callno=None,
                     title=None,
                     author=None,
                     publisher=None,
                     pubyear=None,
                     isbn=None).save()

    return
for c in code:
    start = time.time()
    book(code=c)
    print(c,'걸린시간:', time.time() - start)


