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
    # num = total.count()
    page = request.GET.get('page', '1')

    paginator = Paginator(total, 10)
    page_obj = paginator.get_page(page)

    # gmap
    for list in total:
        print(list.author, list.title)


    # 결과 출력
    context = {
        'total' : page_obj,
    }

    return render(request, 'booksearch.html', context)

