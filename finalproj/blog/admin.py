from django.contrib import admin
from .models import BlogPost, Category, Tag
from accounts.models import UserProfile


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'enabled', 'publish_time', 'press')

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)