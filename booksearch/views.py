from django.shortcuts import render

def booksearch(request):
    return render(request, 'booksearch.html')