from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField#
from accounts.models import UserProfile

# 定義標籤名稱欄位
class Tag(models.Model):
    title = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.title

# 定義分類名稱欄位
class Category(models.Model):
    title = models.CharField(max_length=255, default="")
    def __str__(self):
        return self.title

class BlogPost(models.Model):
    title = models.CharField(max_length=500, default='')
    content = RichTextUploadingField()
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag)
    publish_time = models.DateTimeField(auto_now=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    def __str__(self):
        return self.title


