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
    publish_time = models.DateTimeField(auto_now_add=True)
    enabled = models.BooleanField(default=False)
    press = models.IntegerField(default=0)
    # slug = models.SlugField(default="", null=False)
    def __str__(self):
        return self.title

class BoardUnit(models.Model):
    bblogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    btime = models.DateTimeField(auto_now_add=True)
    bcontent = models.TextField(null=False)
    bauthor = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    btimedelta = models.IntegerField(blank=True, null=True,default=0)
    def __str__(self):
        return self.bcontent

class BoardUnitResponse(models.Model):
    bboardunit = models.ForeignKey(BoardUnit, on_delete=models.CASCADE)
    bresponse = models.TextField(blank=True, default='')
    bresponse_time = models.DateTimeField(blank=True, null=True)
    bresponse_author = models.ForeignKey(UserProfile, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.bresponse