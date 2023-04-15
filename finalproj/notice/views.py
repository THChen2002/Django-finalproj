from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

from notifications.signals import notify
from notifications.models import Notification



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
    # 取得使用者的通知
    notifications = Notification.objects.filter(user=request.user, unread=True)

    # 標記通知為已讀
    notifications.update(unread=False)

    return render(request, 'notifications.html', {'notifications': notifications})