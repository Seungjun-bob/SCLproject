from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Library, Comment
from django.core.paginator import Paginator
from django.contrib.auth.models import User

def board(request) :

    page = request.GET.get('page', 1)
    vlist = Review.objects.all()
    paginator = Paginator(vlist, 10)
    #print(paginator)
    vlistpage = paginator.get_page(page)
    #print(type(vlistpage))
    #for d in vlistpage :
    #    print(type(d), d)
    context = {
        "vlist": vlistpage,
    }
    return render(request, 'board.html', context)

def submit(request):
    print(request.user)
    if not request.user.is_authenticated:
        return redirect('/index/login/')
    else:
        if request.method == "POST":
            title = request.POST['title']
            starpoint = request.POST['starpoint']
            content = request.POST['content']
            author = request.user.id
            lbrry_name = request.POST['lbrry_name']
            lib = Library.objects.get(lbrry_name=lbrry_name)

            data = Review(starpoint=starpoint,
                          title=title,
                          author_id=author,
                          library_id=lib.lbrry_seq_no,
                          content=content,)
            data.save()
            return render(request, 'board.html')
        else:
            return render(request, 'submit.html')

def result(request, pk):
    # result = Review.objects.get(pk=pk)
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


def my_review(request):
    return render(request, 'my_review.html')



