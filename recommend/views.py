from django.shortcuts import render
from libsearch.models import Library
from django.core.paginator import Paginator

def recommend(request):
    search = request.GET.get('search', "")
    library_div = request.GET.get("lbrry_se_name", "")
    library_gu = request.GET.get("code_value", "")
    library_info = Library.objects.all()

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

    # 결과 출력
    context = {
        'total' : page_obj,
        # 'num' : num, # 도서관 검색 출력 수
    }

    return render(request, 'recommend.html', context)


def detail(request):
    return render(request, 'detail.html')
