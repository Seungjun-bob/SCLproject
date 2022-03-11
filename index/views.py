from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.hashers import check_password

def index(request):
    return render(request, 'index.html')

def register(request):
    res_data = None
    if request.method =='POST':
        useremail = request.POST.get('useremail')
        username = request.POST.get('username')
        usernickname = request.POST.get('usernickname')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        res_data = {}
        if User.objects.filter(username=useremail):
            res_data['error']='이미 가입된 아이디(이메일주소)입니다.'
        elif password != re_password:
            res_data['error']='비밀번호가 다릅니다.'
        else:
            user = User.objects.create_user(username = useremail,
                            first_name = username,
                            last_name = usernickname,
                            password = password)
            auth.login(request, user)
            return render(request, 'index.html')
    return render(request, 'register.html', res_data)


def login(request):
    if request.method == "POST":
        useremail = request.POST.get('useremail', None)
        password = request.POST.get('password', None)
        user = auth.authenticate(username=useremail, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index:index')
        else:
            return render(request, 'login.html', {'error': '사용자 아이디 또는 패스워드가 틀립니다.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return render(request, "index.html")

def about(request):
    return render(request, 'about.html')

def changepassword(request):
    if request.method =='POST':
        user = request.user
        password = request.POST['pass']
        new_password = request.POST['new_password']
        new_password2 = request.POST['new_password2']
        print(user.password, password, new_password, new_password2)
        if check_password(password, user.password):
            if new_password == new_password2:
               user.set_password(new_password)
               user.save()
            else:
                '변경할 비밀번호가 일치하지 않습니다.'
        else:
            '현재 비밀번호가 일치하지 않습니다.'
    return render(request, 'change_password.html')
