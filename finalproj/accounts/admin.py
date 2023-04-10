from django.contrib import admin
from .models import UserProfile

# Register your models here.
class studentAdmin(admin.ModelAdmin):
	#list_display = ("stdName", "stdID", "stdSex")
	#list_filter = ("stdSex",)
	search_fields=('user_id')
admin.site.register(UserProfile)