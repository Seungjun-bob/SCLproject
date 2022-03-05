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


def book(code):
    for page in range(1,11):
        open_url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi?serviceKey=0OhBU7ZCGIobDVKDeBJDpmDRqK3IRNF6jlf%2FJB2diFAf%2FfR2czYO9A4UTGcsOwppV6W2HVUeho%2FFPwXoL6DwqA%3D%3D'
        url = open_url + f'&title=&manageCd={code}&numOfRows=100&pageNo=' + str(page)
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
                Book(libname=i['libName'],
                     callno=i['callNo'],
                     title=i['title'],
                     author=i['author'],
                     publisher=i['publisher'],
                     pubyear=i['pubYear'],
                     isbn=None,).save()
            print(i,'페이지완료')
    return

book(code='MA')

