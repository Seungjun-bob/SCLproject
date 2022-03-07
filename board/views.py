from django.shortcuts import render, redirect
from .models import Review, Library , Comment
from django.core.paginator import Paginator


def board(request):
    page = request.GET.get('page', 1)
    vlist = Review.objects.all()
    paginator = Paginator(vlist, 3)
    # print(paginator)
    vlistpage = paginator.get_page(page)
    # print(type(vlistpage))
    # for d in vlistpage :
    #    print(type(d), d)
    context = {
        "vlist": vlistpage,
    }
    return render(request, 'board.html', context)


def submit(request):
    if request.method == "POST":
        title = request.POST['title']
        starpoint = request.POST['starpoint']
        content = request.POST['content']
        author = request.user.id
        library = request.POST['library']
        lib = Library.objects.get(lbrry_name=library)
        data = Review(starpoint=starpoint,
                      title=title,
                      author_id=author,
                      library_id=lib.lbrry_seq_no,
                      content=content, )
        data.save()
        return render(request, 'submit.html')
    else:
        return render(request, 'submit.html')

def my_review(request):
    return render(request, 'my_review.html')

def result(request, pk):
    article = Review.objects.get(pk)
    print(article)
    context = {
        'article': article,
    }
    return render(request, 'result.html',context)

