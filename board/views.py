from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.core.paginator import Paginator
from .models import Board, Comment
from django.contrib.auth.models import User
import time

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

    context = {
        "vlist": vlistpage,
        "comment": comment,
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


def update(request, board_id):
    update = get_object_or_404(Board, id=board_id)
    if request.method == 'GET':
        context = {'update': update}
        return render(request, 'update.html', context)
    else:
        id = update.id
        update.title = request.POST['title1']
        update.content = request.POST['content1']
        author_id = 1
        date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        Board(title=update.title,
              content=update.content,
              author_id=author_id,
              Cdate=date,
              Udate=date,
              id=id).save()
        return redirect('board:result', board_id)

def my_review(request):
    return render(request, 'my_review.html')



