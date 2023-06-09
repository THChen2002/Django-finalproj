"""
Django settings for finalproj project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-*n55vb99k2c8g7m6-stza%6jybhl)6iv+fco+j1jfwg-b5p(x#"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # 自己的應用程式
    'weather',
    'accounts',
    'blog',
    'notice',
    'quiz',

    # allauth
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    #圖形驗證碼
    'captcha',

    # google provider
    'allauth.socialaccount.providers.google',

    # 文章編輯套件
    'ckeditor',
    'ckeditor_uploader',

    #系統通知套件
    'notifications',

    #過濾器
    'django_filters'
]


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "finalproj.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "finalproj.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Taipei'

USE_I18N = True

USE_TZ = True


LOGIN_REDIRECT_URL = '/'  # 登入後的首頁網址

SITE_ID = 1

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [ BASE_DIR / "static" ]
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
CKEDITOR_UPLOAD_PATH = 'upload/'

# 放在django 專案根目录，同时也需要新建media資料夾
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
# CKEDITOR_UPLOAD_PATH = 'upload/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# SMTP Configuration
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  #SMTP伺服器
EMAIL_PORT = 587  #TLS通訊埠號
EMAIL_USE_TLS = True  #開啟TLS(傳輸層安全性)
# EMAIL_HOST_USER = 'ntuedjangoweb@gmail.com'  #寄件者電子郵件
# EMAIL_HOST_PASSWORD = 'vkfvecvufhnvhpfl'  #Gmail應用程式的密碼
# EMAIL_HOST_USER = 'joewu1018@gmail.com'  #寄件者電子郵件
# EMAIL_HOST_PASSWORD = 'llvlmxvbqwjrvllv'  #Gmail應用程式的密碼
EMAIL_HOST_USER = '20230412ntue@gmail.com'  #寄件者電子郵件
EMAIL_HOST_PASSWORD = 'fkcalqnpksjsrlkr'  #Gmail應用程式的密碼

CAPTCHA_NOISE_FUNCTIONS = (
    #'captcha.helpers.noise_null', #没有樣式  
    'captcha.helpers.noise_arcs', #線  
    'captcha.helpers.noise_dots', #點  
)
#CAPTCHA_IMAGE_SIZE = (150, 70) #圖片大小 

#CAPTCHA_BACKGROUND_COLOR = '#00ff00' #背景頻色

#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.random_char_challenge' #圖片為英文字母 
#CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge' #圖片中為數學計算式  
  
#CAPTCHA_LENGTH = 6 #英文字母個數 

#CAPTCHA_TIMEOUT = 1 #時間限制(分) 

CKEDITOR_CONFIGS = {
    'default': {
        'skin': 'moono-lisa',        
    'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],        
    'toolbar_Full': [
            [ 'Source','-','Save','NewPage','DocProps','-','Templates' ],            
            [ 'Cut','Copy','Paste','PasteText','PasteFromWord','-','Undo','Redo' ],          
            [ 'Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton', 'HiddenField','-','BidiLtr','BidiRtl', '-', 'Link','Unlink','Anchor'],'/',  
            [ 'Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak','Iframe' ],          
            [ 'NumberedList','BulletedList','-','Outdent','Indent','-','Blockquote','CreateDiv', '-','JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'],          
            [ 'Bold','Italic','Underline','Strike','Subscript','Superscript','-','RemoveFormat' ],  '/',            
            [ 'Styles','Format','Font','FontSize' ] , [ 'TextColor','BGColor' ] , [ 'Maximize', 'ShowBlocks','-','About' ] ,                         
            ['CodeSnippet'],  #插入程式code按鈕
        ],        
    'toolbar': 'Full',        
    'extraPlugins': 'codesnippet',}   #插入程式code    
}

