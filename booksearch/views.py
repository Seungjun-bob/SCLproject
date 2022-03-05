from django.shortcuts import render
from booksearch.models import Book
from django.core.paginator import Paginator

def booksearch(request):
    search = request.GET.get('search', "")
    library_div = request.GET.get("lbrry_se_name", "")
    library_gu = request.GET.get("code_value", "")
    library_info = Book.objects.all()

    if library_div == "" and library_gu == "" and search == "":
        total = []
    elif library_div=='전체' and library_gu=='전체':
        library_div = ""
        library_gu = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    elif library_div=='전체':
        library_div = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    elif library_gu=='전체':
        library_gu = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    else:
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)

    # paging
    # num = total.count()
    page = request.GET.get('page', '1')

    paginator = Paginator(total, 5)
    page_obj = paginator.get_page(page)

    # gmap
    ydnts = [];
    xcnts = [];
    hname = [];
    for data in total:
            xcnts.append(data.xcnts)
            ydnts.append(data.ydnts)
            hname.append(data.lbrry_name)



    # 결과 출력
    context = {
        'total' : page_obj,
        # 'num' : num, # 도서관 검색 출력 수
        'xcnts' : xcnts,
        'ydnts' : ydnts,
        'hname' : hname
    }

    return render(request, 'booksearch.html', context)


