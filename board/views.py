from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_GET
from django.core.paginator import Paginator
from .models import Review, Library, Comment
from django.contrib.auth.models import User

def board(request) :
    # 데이터를 최신순으로 정렬
    Reivews = Review.objects.all().order_by('-id')

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
            starpoint = request.POST['starpoint']
            content = request.POST['content']
            author = request.user.id
            lbrry_name = request.POST['lbrry_name']

            # 도서관 id 값을 가져오는 코드
            lib = Library.objects.get(lbrry_name=lbrry_name)

            data = Review(starpoint=starpoint,
                          title=title,
                          author_id=author,
                          library_id=lib.lbrry_seq_no,
                          content=content,)
            data.save()
            return redirect('board:result', data.id)
        else:
            return render(request, 'submit.html')

def result(request, pk):
    # Review 클래스에서 id 값에 맞는 데이터 가져옴
    result = get_object_or_404(Review, id=pk)

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
    comment.review_id = pk
    print(author)
    Comment(comment=content,
            user_id=author,
            review_id=pk
            ).save()
    context = {
        'content': content,
        'author': author
    }

    return redirect('board:result', pk)

def delete(request, pk):
    review = Review.objects.get(id=pk)
    review.delete()
    return redirect('/board/')

def update():
    return

def my_review(request):
    return render(request, 'my_review.html')



