from django.shortcuts import render
from booksearch.models import Book
from django.core.paginator import Paginator

def booksearch(request):

    title = request.GET.get('title', "")
    author = request.GET.get("author", "")
    isbn = request.GET.get("isbn", "")
    book_info = Book.objects.all()

    if title == "" and author == "" and isbn == "":
        total = []

    else:
        total = book_info.filter(title__icontains=title,
                                 author__icontains=author,
                                 isbn__icontains=isbn)

    # paging
    page = request.GET.get('page', '1')

    paginator = Paginator(total, 5)
    page_obj = paginator.get_page(page)



    # 결과 출력d
    context = {

        'total' : total,

        'page' :page_obj,

    }

    return render(request, 'booksearch.html', context)



