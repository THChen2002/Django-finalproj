from django.contrib import admin
from .models import UserProfile

# Register your models here.
class AccountAdmin(admin.ModelAdmin):
	list_display = ("user_id", "user_name", "email", "first_name", "last_name")
	#list_filter = ("stdSex",)
	search_fields=('user_id',)
admin.site.register(UserProfile, AccountAdmin)