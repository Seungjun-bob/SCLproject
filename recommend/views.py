from django.shortcuts import render

def recommend(request):
    return render(request, 'recommend.html')

def detail(request):
    return render(request, 'detail.html')
