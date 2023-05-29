from django.contrib import admin
from .models import BlogPost, Category, Tag, BoardUnit, BoardUnitResponse
from accounts.models import UserProfile
import urllib.parse


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'enabled', 'publish_time', 'press')
    # prepopulated_fields = {"slug": ("title",)}
    list_filter = ["category", 'tags']

    # def save_model(self, request, obj, form, change):
    #     obj.title = form.cleaned_data['title']  # 获取表单中的标题
    #     obj.slug = urllib.parse.quote(obj.title)  # 对标题进行编码并赋值给slug字段
    #     super().save_model(request, obj, form, change)

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BoardUnit)
admin.site.register(BoardUnitResponse)
