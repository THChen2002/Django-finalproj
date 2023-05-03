from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import User

from notifications.signals import notify
from notifications.models import Notification
import json
from django.core import serializers



def send_message(request, recipient):
    # 創建通知
    user = request.user
    message = "您有一則新訊息。"
    notify.send(
        sender=user,  # 發送者設定為當前登入的使用者
        recipient=User.objects.get(id=2),  # 接收者設定為當前登入的使用者
        verb='登入成功',  # 設定通知的動作
        description='歡迎回來',  # 設定通知的描述
    )

def view_notifications(request):
    if request.method=="POST":
        data = json.loads(request.body)
        id = data.get('id')
        # id == 0 表示全部標記為已讀 
        if id == 0:
            # 取得使用者的通知
            notifications = Notification.objects.filter(recipient=request.user)
            # 標記通知為已讀
            notifications.update(unread=False)
            return redirect(request.META.get('HTTP_REFERER'))
        else:
            # 取得使用者的通知     
            notification = Notification.objects.filter(id=id)
            # 標記通知為已讀
            notification.update(unread=False)
            notifications = Notification.objects.filter(recipient=request.user, unread=True)
            notifications_data = serializers.serialize('json', notifications)
            request.session['unread_notifications'] = notifications_data
        # 返回空的 HTTP 回應
        return HttpResponse('')
    else:
        return render(request, 'accounts/index.html')