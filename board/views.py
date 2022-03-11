from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.core.paginator import Paginator
from .models import Board, Comment
from django.contrib.auth.models import User
from django.db.models import Q

def board(request) :
    # 데이터를 최신순으로 정렬
    boards = Board.objects.all().order_by('-id')

    # 유저 정보
    users = User.objects.all()

    # 검색 처리
    search = request.GET.get('search', "")
    type = request.GET.get('type', "")

    if type == "전체":
        total = boards.filter(Q(title__icontains=search) | Q(content__icontains=search))
    elif type == "제목":
        total = boards.filter(title__icontains=search)
    elif type == "내용":
        total = boards.filter(content__icontains=search)
    else:
        total = boards.filter(Q(title__icontains=search) | Q(content__icontains=search))

    # 페이징 처리리
    page = request.GET.get('page', 1)
    paginator = Paginator(total, 15)
    listpage = paginator.get_page(page)

    context = {
        "total": listpage,
        "users": users,
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
    board_user = board.author_id
    user_name = User.objects.get(pk=board_user).last_name

    comments = board.comment_set.order_by('-id').all()

    context = {
        'board': board,
        'user_name': user_name,
        'comments': comments
    }
    return render(request, 'result.html', context)

def delete(request, board_id):
    board = Board.objects.get(id=board_id)
    board.delete()
    return redirect('/board/')

def edit(request, board_id):
    board = Board.objects.get(id=board_id)
    context = {'board': board}
    return render(request, 'update.html', context)

def update(request, board_id):
    title = request.POST.get('title')
    content = request.POST.get('content')
    board = Board.objects.get(id=board_id)
    board.title = title
    board.content = content
    board.save()
    return redirect('board:result', board_id)


def comment_create(request, board_id):

    content = request.POST['content']
    author = request.user.id

    Comment(comment=content,
            user_id=author,
            board_id=board_id,
            ).save()

    return redirect('board:result', board_id)

def comment_delete(request, board_id, comment_id):
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return redirect('board:result', board_id)


def my_review(request):
    return render(request, 'my_review.html')




