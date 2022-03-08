from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.core.paginator import Paginator
from .models import Board, Comment
from django.contrib.auth.models import User

def board(request) :
    # 데이터를 최신순으로 정렬
    Reivews = Board.objects.all().order_by('-id')

    # 유저 정보
    users = User.objects.all()

    # 페이징 처리리
    page = request.GET.get('page', 1)
    paginator = Paginator(Reivews, 15)
    vlistpage = paginator.get_page(page)

    context = {
        "vlist": vlistpage,
        "users": users,
    }
    return render(request, 'board.html', context)

def submit(request):
    if not request.user.is_authenticated:
        return redirect('/index/login/')
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

def result(request, pk):
    # Board 클래스에서 id 값에 맞는 데이터 가져옴
    result = get_object_or_404(Board, id=pk)

    # 유저 정보 가져오기
    user_pk = result.author_id
    user_name = User.objects.get(pk=user_pk).last_name

    comments = result.comment_set.order_by('-id').all()

    context = {
        'result': result,
        'user_name': user_name,
        'comments': comments
    }
    return render(request, 'result.html', context)

# @require_http_methods(['POST'])

def comment(request, pk):
    content = request.POST['content']
    author = request.user.id
    comment = Comment()
    Comment.Board_id = pk
    print(Comment.Board_id)
    Comment(comment=content,
            user_id=author,
            board_id=pk,
            ).save()
    context = {
        'content': content,
        'author': author,
        'board_id': pk,
    }

    return redirect('board:result', pk)


def delete(request, pk):
    board = Board.objects.get(id=pk)
    board.delete()
    return redirect('/board/')


def comment_delete(request, pk):
    comment = Comment.objects.get(id=pk)
    comment.delete()
    return redirect('/board/', pk)


def update(request, pk):
    update = get_object_or_404(Board, id=pk)
    if request.method == 'GET':
        context = {'update': update}
        return render(request, 'update.html', context)
    else:
        id = update.id
        update.title = request.POST['title1']
        update.content = request.POST['content1']
        author_id = 1
        date = "2022-02-02 22:22"
        Board(title=update.title,
              content=update.content,
              author_id=author_id,
              Udate=date,
              id=id).save()
        return redirect('board:result', pk)

def my_review(request):
    return render(request, 'my_review.html')



