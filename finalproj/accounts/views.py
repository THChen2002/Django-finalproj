from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount
from accounts.models import UserProfile

from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

import json
from django.http import JsonResponse
from django.utils.crypto import get_random_string


from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.decorators import user_passes_test
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages
from django.urls import reverse


# Create your views here.
#def login(request):
#    return render(request, 'accounts/login.html')

# 首頁
@login_required(login_url="Login")
def index(request):   
    userID = request.user.id
    #unit = UserProfile.objects.get(user_id=userID) 
    #profile_pic_url = unit.profile_pic.url
    try:
        # Get the user's social account for the provider
        social_account = SocialAccount.objects.get(user = userID)
        # Get the user's profile picture
        picture_url = social_account.extra_data.get('picture')
    except SocialAccount.DoesNotExist:
        picture_url = '/static/images/user_default.png'
        
    request.session['picture_url'] =  picture_url
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

#使用者點及變更頭像
def upload_photo(request):
    if request.method == 'POST':
        unit = UserProfile.objects.get(user_id=request.user.id)
        unit.profile_pic = request.FILES['photo']
        unit.save()
        return JsonResponse({'message': 'Upload Success!'})
     

#取得所有sessions
def get_allsessions(request):
	if request.session!=None:
		strsessions=""
		for key1,value1 in request.session.items():
			strsessions= strsessions + key1 + ":" + str(value1) + "<br>"
		return HttpResponse(strsessions)
	else:
		return HttpResponse('Session 不存在!')	


#忘記密碼頁面
def forgot_password(request):
    if request.method == 'POST':
        email = request.POST['email']
        try:
            user = User.objects.get(email=email)
            # 生成一個隨機的密碼重置令牌
            token = default_token_generator.make_token(user)
            # 將令牌和使用者資訊保存到資料庫
            user.reset_password_token = token
            user.save()
            # 發送包含重置連結的電子郵件

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            reset_link = request.build_absolute_uri('/reset/confirm/'+ uidb64 + '/' + token)
            send_mail(
                '密碼重置請求',
                '請點擊以下連結來重置您的密碼: ' + reset_link,
                settings.EMAIL_HOST_USER,  # 寄件者
                [email],
                fail_silently=False,
            )
            return render(request, 'accounts/email_success.html')
        except User.DoesNotExist:
            return render(request, 'accounts/email_error.html')
    return render(request, 'accounts/forgot_password.html')


#使用者收信後的連結頁面
def password_reset_confirm(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        # 顯示密碼重設表單
        form = SetPasswordForm(user=user)
        if request.method == 'POST':
            form = SetPasswordForm(user=user, data=request.POST)
            if form.is_valid():
                form.save()
                user.reset_password_token = None
                user.save()
                messages.success(request, '您的密碼已成功重設。')
                return redirect('password_reset_complete')
        return render(request, 'accounts/reset_password_confirm.html', {'form': form})
    else:
        # 顯示錯誤訊息
        messages.error(request, '密碼重設連結無效或已過期。')
        return redirect('forgot_password')
    
#密碼重設成功頁面
def password_reset_complete(request):
    return render(request, 'accounts/reset_password_complete.html')


#about頁面
def about(request):
     return render(request, 'about.html')
