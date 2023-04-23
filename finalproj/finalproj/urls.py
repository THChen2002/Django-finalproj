"""finalproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import weather.views as weather
import accounts.views as accounts
import blog.views as blog
import notice.views as notice
import notifications.urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", accounts.index),
    path('accounts/', include('allauth.urls')),
    path('captcha/', include('captcha.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('', accounts.index, name='Index'),
    path('register/', accounts.sign_up, name='Register'),
    path('login/', accounts.sign_in, name='Login'),
    path('logout/', accounts.log_out, name='Logout'),
    path('profile/', accounts.profile, name='Profile'),
    path('photo', accounts.upload_photo, name='Photo'),

    path('get_allsessions/', accounts.get_allsessions),
    # 忘記密碼頁面
    path('forgot_password/', accounts.forgot_password, name='forgot_password'),
    # 密碼重設確認頁面
    path('reset/confirm/<uidb64>/<token>/', accounts.password_reset_confirm, name='password_reset_confirm'),
    # 密碼重設完成頁面
    path('reset/complete/', accounts.password_reset_complete, name='password_reset_complete'),
    path('about/', accounts.about),
    
    path('inbox/notifications/', include(notifications.urls, namespace='notifications')),
    path('notice', notice.view_notifications, name='view_notifications'),
    
    # path('notice/', include('notice.urls', namespace='notice')),

    path('apple-blog/', blog.blog),

    path('weather/', weather.weather),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
