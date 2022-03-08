from django.shortcuts import render
from libsearch.models import Library
from django.core.paginator import Paginator

def libsearch(request):
    search = request.GET.get('search', "")
    library_div = request.GET.get("lbrry_se_name", "")
    library_gu = request.GET.get("code_value", "")
    library_info = Library.objects.all()

    if library_div == "" and library_gu == "" and search == "":
        total = []
    elif library_div == '전체' and library_gu == '전체':
        library_div = ""
        library_gu = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    elif library_div == '전체':
        library_div = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    elif library_gu == '전체':
        library_gu = ""
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)
    else:
        total = library_info.filter(lbrry_se_name__icontains=library_div,
                                    code_value__icontains=library_gu,
                                    lbrry_name__icontains=search)


    # paging


    page = request.GET.get('page', '1')

    paginator = Paginator(total, 5)
    page_obj = paginator.get_page(page)

    # gmap
    ydnts = []; xcnts = []; hname = []; adres = []; hmpg_url = [];

    for i in hmpg_url:
        if i == None:
            print(i)


    for data in total:
            xcnts.append(data.xcnts)
            ydnts.append(data.ydnts)
            hname.append(data.lbrry_name)
            adres.append(data.adres)
            hmpg_url.append(data.hmpg_url)
    num = len(total)
    # 결과 출력
    context = {
        'total' : page_obj,
        'num' : num, # 도서관 검색 출력 수
        'xcnts' : xcnts,
        'ydnts' : ydnts,
        'hname' : hname,
        'adres' : adres,
        'hmpg_url' : hmpg_url,
    }
    return render(request, 'libsearch.html', context)

def detail_library(request, pk):
    detail_library = Library.objects.get(lbrry_seq_no=pk)
    # gmap
    ydnts = [];
    xcnts = [];
    hname = [];
    adres = [];
    hmpg_url = [];

    for i in hmpg_url:
        if i == None:
            print(i)

    # 결과 출력
    context = {
        'detail_library': detail_library,
        'xcnts': xcnts,
        'ydnts': ydnts,
        'hname': hname,
        'adres': adres,
        'hmpg_url': hmpg_url,
    }
    return render(request, 'detail_l.html', context)
