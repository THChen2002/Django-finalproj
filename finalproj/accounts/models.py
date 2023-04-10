from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=50)
    #user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_pic = models.ImageField(upload_to='static/images/profile_pics/', blank=True, null=True)
    first_name = models.CharField(max_length=50 , null=True)
    last_name = models.CharField(max_length=50 , null=True)
    email = models.EmailField(max_length=254 , null=True)
    
    def __str__(self):
        return self.user_id
