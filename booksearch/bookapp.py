import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SCLproject.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

import urllib.request as MyURL
from bs4 import BeautifulSoup
from booksearch.models import Book

url = 'http://openapi-lib.sen.go.kr/openapi/service/lib/openApi?serviceKey=0OhBU7ZCGIobDVKDeBJDpmDRqK3IRNF6jlf%2FJB2diFAf%2FfR2czYO9A4UTGcsOwppV6W2HVUeho%2FFPwXoL6DwqA%3D%3D&title=&manageCd=MB&numOfRows=1000&pageNo=1'

response = MyURL.urlopen(url)
book = BeautifulSoup(response, "html.parser")

# for data in book.findAll('item'):
#     Book(isbn = data.isbn.string,
#         author = data.author.string,
#         libname = data.libname.string,
#         pubyear = data.pubyear.string,
#         publisher = data.publisher.string,
#         callno=data.callno.string,
#         title=data.title.string,
#          ).save()

#
# for data in book.findAll('item'):
#     if data.isbn is not None:
#         print("1 :" + data.isbn.string)
#     else :
#         print("-----------"*10)
#     if data.author is not None:
#         print("2 :" + data.author.string)
#     else :
#         print("-----------"*10)
#     if data.libname is not None:
#         print("3 :" + data.libname.string)
#     else :
#         print("-----------"*10)
#     if data.pubyear is not None:
#         print("4 :" + data.pubyear.string)
#     else :
#         print("-----------"*10)
#     if data.publisher is not None:
#         print("5 :" + data.publisher.string)
#     else :
#         print("-----------"*10)
#     if data.callno is not None:
#         print("6 :" + data.callno.string)
#     else :
#         print("-----------"*10)
#     if data.title is not None:
#         print("7 :" + data.title.string)
#     else :
#         print("-----------"*10)

# for data in book.findAll('item'):
#     if data.isbn is not None:
#         print("1 :" + data.isbn.string)
#     if data.author is not None:
#         print("2 :" + data.author.string)
#     if data.libname is not None:
#         print("3 :" + data.libname.string)
#     if data.pubyear is not None:
#         print("4 :" + data.pubyear.string)
#     if data.publisher is not None:
#         print("5 :" + data.publisher.string)
#     if data.callno is not None:
#         print("6 :" + data.callno.string)
#     if data.title is not None:
#         print("7 :" + data.title.string)

# for data in book.findAll('item'):
#     if data.isbn is not None:
#         Book(isbn = data.isbn.string).save()
#     if data.author is not None:
#         Book(author = data.author.string).save()
#     if data.libname is not None:
#         Book(libname = data.libname.string).save()
#     if data.pubyear is not None:
#         Book(pubyear = data.pubyear.string).save()
#     if data.publisher is not None:
#         Book(publisher = data.publisher.string).save()
#     if data.callno is not None:
#         Book(callno=data.callno.string).save()
#     if data.title is not None:
#         Book(title=data.title.string).save()

