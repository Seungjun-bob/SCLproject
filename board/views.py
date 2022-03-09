from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.core.paginator import Paginator
from .models import Board, Comment
from django.contrib.auth.models import User

def board(request) :
    # 데이터를 최신순으로 정렬
    boards = Board.objects.all().order_by('-id')
    comment = Comment.objects.all()

    # 유저 정보
    users = User.objects.all()

    # 페이징 처리리
    page = request.GET.get('page', 1)
    paginator = Paginator(boards, 15)
    vlistpage = paginator.get_page(page)

    # 검색 처리
    search = request.GET.get('search', "")
    type = request.GET.get('type', "")

    if type == "전체":
        total = boards.filter(title__icontains=search,
                              content__icontains=search)
    elif type == "제목":
        total = boards.filter(title__icontains=search)
    elif type == "내용":
        total = boards.filter(content__icontaions=search)
    else:
        total = boards.filter(title__icontains=search,
                              content__icontains=search)
    print(total)
    context = {
        "vlist": vlistpage,
        "comment": comment,
        "users": users,
        "total": total
    }

    return render(request, 'board.html', context)


def submit(request):
    if not request.user.is_authenticated:

        return redirect('index:login')
    else:
        if request.method == "POST":
            title = request.POST['title']
            content = request.POST['content']
            author = request.user.id

            data = Board(title=title,
                         author_id=author,
                         content=content,)
            data.save()
            return redirect('board:result', data.id)
        else:
            return render(request, 'submit.html')

def result(request, board_id):
    # Board 클래스에서 id 값에 맞는 데이터 가져옴
    board = get_object_or_404(Board, id=board_id)

    # 유저 정보 가져오기
    user_pk = board.author_id
    user_name = User.objects.get(pk=user_pk).last_name

    comments = board.comment_set.order_by('-id').all()
    print(comments)
    context = {
        'board': board,
        'user_name': user_name,
        'comments': comments
    }
    return render(request, 'result.html', context)

# @require_http_methods(['POST'])

def comment_create(request, board_id):
    content = request.POST['content']
    author = request.user.id

    Comment(comment=content,
            user_id=author,
            board_id=board_id,
            ).save()

    return redirect('board:result', board_id)


def delete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('/board/')


def comment_delete(request, board_id, comment_id):
    print(board_id, comment_id)
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('board:result', board_id)


def edit(request, board_id):
    board = Board.objects.get(id=board_id)
    print(11)
    context = {'board': board}
    return render(request, 'update.html', context)

def update(request, board_id):
    print(111)
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board.objects.get(id=board_id)
    board.title = title
    board.content = content
    board.save()
    return redirect('board:result', board_id)


def my_review(request):
    return render(request, 'my_review.html')

def search(request):


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



