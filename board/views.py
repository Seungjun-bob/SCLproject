from django.shortcuts import render
from .models import Review
from django.core.paginator import Paginator

def board(request) :
    page = request.GET.get('page', 1)
    vlist = Review.objects.all()
    paginator = Paginator(vlist, 3)
    #print(paginator)
    vlistpage = paginator.get_page(page)
    #print(type(vlistpage))
    #for d in vlistpage :
    #    print(type(d), d)
    context = {"vlist": vlistpage}
    return render(request, 'board.html', context)


def my_review(request):
    return render(request, 'my_review.html')


def submit(request):
    return render(request, 'submit.html')


def result(request):
    return render(request, 'result.html')
