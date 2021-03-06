from django.shortcuts import render,redirect
from app.models import User, PictureFile
from .forms import UserForm, RegisterForm
import hashlib
from django.http import HttpResponse
from sympy import ExactQuotientFailed, re
    
# 登录
def login(request):
    if request.session.get('is_login', None):
        return redirect("/index/")
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = User.objects.get(username=username)
                if user.password == hash_code(password):  # 哈希值和数据库内的值进行比对
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.username
                    return redirect('/index/')
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        # 登录状态不允许注册。你可以修改这条原则！
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():  # 获取数据
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            sex = register_form.cleaned_data['sex']
            if password1 != password2:  # 判断两次密码是否相同
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = User.objects.filter(username=username)
                if same_name_user:  # 用户名唯一
                    message = '用户已经存在，请重新选择用户名！'
                    return render(request, 'register.html', locals())
                same_email_user = User.objects.filter(email=email)
                if same_email_user:  # 邮箱地址唯一
                    message = '该邮箱地址已被注册，请使用别的邮箱！'
                    return render(request, 'register.html', locals())

                # 当一切都OK的情况下，创建新用户

                new_user = User.objects.create()
                new_user.username = username
                new_user.password = hash_code(password1)  # 使用加密密码
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect('login')  # 自动跳转到登录页面
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

def logout(request):
    if not request.session.get('is_login',None):
        return redirect('login')
    request.session.flush()

    return redirect('login')

def hash_code(s, salt='mysite_login'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def index(request):
    pass
    return render(request, 'index.html', locals())

def picture(request):
    if request.method == "GET":
        return render(request, 'picture.html')
    title = request.POST['title']
    file = request.FILES['picture']
    try:
        pf = PictureFile.objects.create(title=title,picture=file)
        request.session['pf'] = pf.picture.url
    except ExactQuotientFailed as e:
        return HttpResponse('上传失败！')
    return redirect('/stylize')

def video(request):
    if request.method == "GET":
        return render(request, 'video.html')
    else:
        title = request.POST['video']
        file = request.FILES['picture']
        try:
            pf = PictureFile.objects.create(title=title, picture=file)
            request.session['pf'] = pf.picture.url
        except ExactQuotientFailed as e:
            return HttpResponse('上传失败')
        return redirect('/stylize')

def upload(request):
    if request.method == "POST":
        title = request.POST['title']
        url = '/stylize/'
        if request.FILES.get('picture', False):
            file = request.FILES['picture']
            url = url + 'picture'
        elif request.FILES.get('video', False):
            file = request.FILES['video']
            url = url + 'video'
        try:
            pf = PictureFile.objects.create(title=title, picture=file)
            request.session['pf'] = pf.picture.url
        except ExactQuotientFailed as e:
            return HttpResponse('上传失败')
        return redirect(url)

# 视频预处理

def preprocess(request):
    if request.method == "POST":
        command = ''
        return

# 处理视频的风格化
def stylize(request, type):
    if request.method == "POST":
        originPath = request.POST['originPath']
        print(originPath)
        # todo 这里根据type做风格化处理
        return render(request, 'stylize.html', context={'path':'somepath', 'type':type, 'res':['/media/001.png']})
    else:
        return render(request, 'stylize.html', context={'type': type})


