from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse

from login.forms import UserForm, RegisterForm
from login.models import User


def index(request):

    return render(request, 'login/index.html')


def login(request):
    if request.session.get('is_login',None):
        return redirect(reverse('index'))

    if request.method == 'POST':
        login_form = UserForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            print(login_form.cleaned_data)
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(name = username)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect(reverse('index'))
                else:
                    message='密码不正确！'
            except:
                message = '用户不存在！'
        return render(request,'login/login.html', locals())

    login_form = UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login',None):
        #登录正态下不允许注册
        return redirect(reverse('index'))

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:
                message = '两次密码不一致！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = User.objects.filter(name = username)
                if same_name_user:
                    message = '用户已存在，请重新选择用户！'
                    return render(request, 'login/register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())
                message = "注册成功！"
                # 当一切都OK的情况下，创建新用户
                # 创建用户信息//有问题：放在创建用户表后面会出现DJANGO pymysql.err.IntegrityError:
                # (1062, "Duplicate entry '' for key 'user_name'")

                # 创建用户表
                new_user = User.objects.create()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()

                return redirect(reverse('login'))

    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        #如果你没有登录，就不需要登出了
        return redirect(reverse('index'))
    request.session.flush()
    # 或者使用下面的方法
    # del request.session['is_login']
    # del request.session['user_id']
    # del request.session['user_name']

    return redirect(reverse('index'))