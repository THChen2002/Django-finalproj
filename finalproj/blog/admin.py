from django.contrib import admin
from .models import BlogPost, Category, Tag, BoardUnit, BoardUnitResponse
from accounts.models import UserProfile


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'enabled', 'publish_time', 'press')
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ["category", 'tags']

admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(BoardUnit)
admin.site.register(BoardUnitResponse)