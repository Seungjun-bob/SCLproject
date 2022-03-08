from django.shortcuts import render
from recommend.models import Recommend
from django.core.paginator import Paginator

def recommend(request):
    search = request.GET.get('search', "")
    recomYear = request.GET.get("recomYear", "")
    recomMonth = request.GET.get("recomMonth", "")
    drCodeName = request.GET.get("drCodeName", "")
    recom_info = Recommend.objects.all()

    if search == "" and recomYear == "" and recomMonth == "" and drCodeName == "":
        total = []
    elif recomYear=='전체' and recomMonth=='전체' and drCodeName=='전체':
        recomYear = ""
        recomMonth = ""
        drCodeName = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif recomYear=='전체' and recomMonth=='전체':
        recomYear = ""
        recomMonth = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif recomYear=='전체' and drCodeName=='전체':
        recomYear = ""
        drCodeName = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif recomMonth=='전체' and drCodeName=='전체':
        recomMonth = ""
        drCodeName = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif recomMonth=='전체':
        recomMonth = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif recomYear=='전체':
        recomYear = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    elif drCodeName=='전체':
        drCodeName = ""
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)

    else:
        total = recom_info.filter(recomYear__icontains=recomYear,
                                  recomMonth__icontains=recomMonth,
                                  drCodeName__icontains=drCodeName,
                                  recomtitle__icontains=search)



    # paging
    num = len(total)
    page = request.GET.get('page', '1')

    paginator = Paginator(total, 5)
    page_obj = paginator.get_page(page)

    # 결과 출력
    context = {
        'total' : page_obj,
        'num' : num,
    }


    return render(request, 'recommend.html', context)

    #

def detail(request, pk):
    detail = Recommend.objects.get(recomNo=pk)
    context = {
        'detail': detail,
    }
    return render(request, 'detail.html', context)
