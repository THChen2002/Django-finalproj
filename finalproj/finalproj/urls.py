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
import weather.views as weather
import accounts.views as accounts

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", accounts.index),
    path('accounts/', include('allauth.urls')),
    path('', accounts.index, name='Index'),
    path('register', accounts.sign_up, name='Register'),
    path('login', accounts.sign_in, name='Login'),
    path('logout', accounts.log_out, name='Logout'),
]
