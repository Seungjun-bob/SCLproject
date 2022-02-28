from django.shortcuts import render

def board(request):
    return render(request, 'board.html')

def my_review(request):
    return render(request, 'my_review.html')

def submit(request):
    return render(request, 'submit.html')