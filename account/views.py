from django.shortcuts import render

def register(request):

def login(request):


def about(request):
    return render(request, 'about.html')

def changepassword(request):
    return render(request, 'change_password.html')


