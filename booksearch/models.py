from django.db import models
'''
libname: 소장도서관(이름)
callno: 청구기호
title: 제목
author: 저작자
publisher: 발행자(출판사)
pubyear: 발행년도
isbn: 낱권ISBN
'''
class Book(models.Model):
    libname = models.CharField(max_length=45, null=True)
    callno = models.CharField(max_length=45, null=True)
    title = models.CharField(max_length=45, null=True)
    author = models.CharField(max_length=45, null=True)
    publisher = models.CharField(max_length=45, null=True)
    pubyear = models.CharField(max_length=45, null=True)
    isbn = models.CharField(max_length=45, null=True)

class Test(models.Model):
    libname = models.CharField(max_length=45, null=True)
    callno = models.CharField(max_length=45, null=True)
    title = models.CharField(max_length=45, null=True)
    author = models.CharField(max_length=45, null=True)
    publisher = models.CharField(max_length=45, null=True)
    pubyear = models.CharField(max_length=45, null=True)
    isbn = models.CharField(max_length=45, null=True)
