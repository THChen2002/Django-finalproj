from django.contrib import admin
from .models import UserProfile

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
	list_display = ("id", "user", "user_name", "email", "first_name", "last_name")
	#list_filter = ("stdSex",)
	search_fields=('id',)
admin.site.register(UserProfile, AccountAdmin)