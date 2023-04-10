from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

import json
from django.http import JsonResponse

from accounts.models import UserProfile

# Create your views here.
#def login(request):
#    return render(request, 'accounts/login.html')

# 首頁
@login_required(login_url="Login")
def index(request):   
    userID = request.user.id
    unit = UserProfile.objects.get(user_id=userID) 
    profile_pic_url = unit.profile_pic.url
    try:
        # Get the user's social account for the provider
        social_account = SocialAccount.objects.get(user = userID)
        # Get the user's profile picture
        picture_url = social_account.extra_data.get('picture')
    except SocialAccount.DoesNotExist:
        picture_url = '/static/images/user_default.png'
        
    request.session['picture_url'] =  profile_pic_url
    return render(request, 'accounts/index.html', locals())


# 註冊
def sign_up(request):

    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            # 電子郵件內容樣板
            email_template = render_to_string(
                'accounts/signup_success_email.html',
                {'username': request.user.username}
            )

            email = EmailMessage(
                '註冊成功通知信',  # 電子郵件標題
                email_template,  # 電子郵件內容
                settings.EMAIL_HOST_USER,  # 寄件者
                [request.POST.get("email")]  # 收件者
            )

            email.fail_silently = False
            email.send()

            return redirect('/login')

    context = {
        'form': form
    }

    return render(request, 'accounts/register.html', context)


# 登入
def sign_in(request):

    form = LoginForm()

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        remember_me = request.POST.get("remember_me")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)  # <-- Here if the remember me is False, that is why expiry is set to 0 seconds. So it will automatically close the session after the browser is closed.

                # else browser session will be as long as the session  cookie time "SESSION_COOKIE_AGE"

            return redirect('/')  # 導向到首頁

    context = {
        'form': form,
    }

    return render(request, 'accounts/login.html', context)


# 登出
def log_out(request):

    logout(request)
    return redirect('/')

#個人檔案頁面
def profile(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form_id = data.get('form_id')
        if form_id == 'photo-form':
            unit = UserProfile.objects.get(user_id=request.user.id) 
            photo = data.get('photo')
            unit.profile_pic = photo
            unit.save()
        else:
            email = data['data']['email']
            first_name = data['data']['first_name']
            last_name = data['data']['last_name']
            user = request.user
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user.save()
        return redirect('/profile')
    else:
        user = request.user
        email = user.email
        first_name = user.first_name
        last_name = user.last_name
    return render(request, 'accounts/profile.html', locals())

#取得所有sessions
def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	

#about頁面
def about(request):
     return render(request, 'about.html')
