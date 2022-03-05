from django.shortcuts import render
from booksearch.models import Book
from django.core.paginator import Paginator

def booksearch(request):

    title = request.GET.get('title', "")
    authorsearch = request.GET.get("authorsearch", "")
    isbnsearch = request.GET.get("isbnsearch", "")
    book_info = Book.objects.all()

    if title == "" and authorsearch == "" and isbnsearch == "":
        total = []

    elif title=='' and authorsearch=='':
        title = ""
        authorsearch = ""
        total = book_info.filter(title__icontains=title,
                                    authorsearch__icontains=authorsearch,
                                    isbnsearch__icontains=isbnsearch)

    elif title == '' and isbnsearch == '':
        title = ""
        isbnsearch = ""
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)

    elif isbnsearch == '' and authorsearch == '':
        isbnsearch = ""
        authorsearch = ""
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)
    elif authorsearch == '':
        authorsearch = ""
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)

    elif title == '':
        title = ""
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)

    elif isbnsearch == '':
        isbnsearch = ""
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)

    else:
        total = book_info.filter(title__icontains=title,
                                 authorsearch__icontains=authorsearch,
                                 isbnsearch__icontains=isbnsearch)

    # paging
    # num = total.count()
    page = request.GET.get('page', '1')

    paginator = Paginator(total, 10)
    page_obj = paginator.get_page(page)

    # gmap
    title = [];
    authorsearch = [];
    libname = [];
    callno = [];
    pubyear = [];
    publisher = [];
    isbnsearch = [];

    for data in total:
        isbnsearch.append(data.isbnsearch)
        authorsearch.append(data.authorsearch)
        libname.append(data.libname)
        callno.append(data.callno)
        pubyear.append(data.pubyear)
        publisher.append(data.publisher)
        title.append(data.title)



    # 결과 출력
    context = {

        'total' : total,
        # 'num' : num, # 도서관 검색 출력 수
        'isbnsearch' : isbnsearch,
        'authorsearch' : authorsearch,
        'libname' : libname,
        'callno': callno,
        'title': title,
        'publisher': publisher,
        'pubyear': pubyear,

    }

    return render(request, 'booksearch.html', context)



