from django.shortcuts import render, redirect, get_object_or_404
from libsearch.models import Library, LibraryComment
from django.core.paginator import Paginator
from django.contrib.auth.models import User

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


def detail_library(request, library_id):
    detail_library = Library.objects.get(lbrry_seq_no=library_id)
    library_detail = get_object_or_404(Library, lbrry_seq_no=library_id)
    comments = library_detail.librarycomment_set.order_by('-id').all()



    # gmap
    ydnts = [];
    xcnts = [];
    hname = [];
    adres = [];
    hmpg_url = [];


    for i in hmpg_url:
        if i == None:
            print(i)

    # 댓글 작성자 구현
    all_user = User.objects.all()
    for comment in comments:
        user_info = all_user.filter(id=comment.user_id)
        for user in user_info:
            user_name = user.last_name

    context = {

    }
    if comments:
        context = {
            'user_name': user_name,
            'detail_library': detail_library,
            'library_detail': library_detail,
            'xcnts': xcnts,
            'ydnts': ydnts,
            'hname': hname,
            'adres': adres,
            'hmpg_url': hmpg_url,
            'comments': comments,
        }
    else:
        context = {
            'detail_library': detail_library,
            'library_detail': library_detail,
            'xcnts': xcnts,
            'ydnts': ydnts,
            'hname': hname,
            'adres': adres,
            'hmpg_url': hmpg_url,
            'comments': comments,
        }

    return render(request, 'detail_l.html', context)



def comment_create(request, library_id):
    content = request.POST['content']
    author = request.user.id
    score = request.POST['score']

    library_detail = get_object_or_404(Library, lbrry_seq_no=library_id)
    comments = library_detail.librarycomment_set.order_by('-id').all()
    sum = 0
    avg = 0
    for comment in comments:
        sum += comment.score
        if comments != 0:
            avg = (sum / len(comments)) * 20
        else:
            pass
    print(library_detail.lbrry_seq_no)

    LibraryComment(comment=content,
                     user_id=author,
                     library_id=library_id,
                   score=score,
                   ).save()

    Library(avg=avg,
            lbrry_name=library_detail.lbrry_name,
            gu_code=library_detail.gu_code,
            code_value=library_detail.code_value,
            adres=library_detail.adres,
            tel_no=library_detail.tel_no,
            hmpg_url=library_detail.hmpg_url,
            op_time=library_detail.op_time,
            fdrm_close_date=library_detail.fdrm_close_date,
            lbrry_se_name=library_detail.lbrry_se_name,
            xcnts=library_detail.xcnts,
            ydnts=library_detail.ydnts,
            lbrry_seq_no=library_detail.lbrry_seq_no).save()



    return redirect('libsearch:detail_l', library_id)


def comment_delete(request, library_id, comment_id):
    print(library_id, comment_id)
    comment = LibraryComment.objects.get(id=comment_id)
    comment.delete()
    library_detail = get_object_or_404(Library, lbrry_seq_no=library_id)
    comments = library_detail.librarycomment_set.order_by('-id').all()
    sum = 0
    avg = 0
    for comment in comments:
        sum += comment.score
        if comments != 0:
            avg = (sum / len(comments)) * 20
        else:
            avg = 0
    Library(avg=avg,
            lbrry_name=library_detail.lbrry_name,
            gu_code=library_detail.gu_code,
            code_value=library_detail.code_value,
            adres=library_detail.adres,
            tel_no=library_detail.tel_no,
            hmpg_url=library_detail.hmpg_url,
            op_time=library_detail.op_time,
            fdrm_close_date=library_detail.fdrm_close_date,
            lbrry_se_name=library_detail.lbrry_se_name,
            xcnts=library_detail.xcnts,
            ydnts=library_detail.ydnts,
            lbrry_seq_no=library_detail.lbrry_seq_no).save()
    return redirect('libsearch:detail_l', library_id)

