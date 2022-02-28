from django.shortcuts import render

def register(request):
    return render(request, 'register.html')

def about(request):
    return render(request, 'about.html')

def changepassword(request):
    return render(request, 'change_password.html')
