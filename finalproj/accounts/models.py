from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    profile_pic = models.ImageField(upload_to='static/images/profile_pics/',blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    GENDER_CHOICES = (
        ('M', '男性'),
        ('F', '女性'),
    )
    address = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    birth_date = models.DateField(blank=True,null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    OCCUPATION_CHOICES = (
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('engineer', 'Engineer'),
        ('developer', 'Developer'),
        ('designer', 'Designer'),
        ('accountant', 'Accountant'),
        ('electrician', 'Electrician'),
        ('scientist', 'Scientist'),
        ('programmer', 'Programmer'),
        ('data scientist', 'Data Scientist'),
        ('IT consultant', 'IT Consultant'),
        ('systems analyst', 'Systems Analyst'),
        ('network administrator', 'Network Administrator'),
        ('web developer', 'Web Developer'),
        ('software engineer', 'Software Engineer'),
        ('database administrator', 'Database Administrator'),
        ('cybersecurity analyst', 'Cybersecurity Analyst'),
        ('artificial intelligence specialist', 'Artificial Intelligence Specialist'),
        ('robotics engineer', 'Robotics Engineer'),
        ('game developer', 'Game Developer'),
        ('mobile app developer', 'Mobile App Developer'),
        ('UI/UX designer', 'UI/UX Designer'),
        ('network engineer', 'Network Engineer'),
        ('cloud computing specialist', 'Cloud Computing Specialist'),
        ('computer systems analyst', 'Computer Systems Analyst'),
        ('IT project manager', 'IT Project Manager'),
        ('network architect', 'Network Architect'),
        ('software tester', 'Software Tester'),
        ('data analyst', 'Data Analyst'),
        ('database developer', 'Database Developer'),
        ('system administrator', 'System Administrator'),
        ('front-end developer', 'Front-end Developer'),
        ('back-end developer', 'Back-end Developer'),
        ('full-stack developer', 'Full-stack Developer'),
        ('data engineer', 'Data Engineer'),
        ('embedded systems engineer', 'Embedded Systems Engineer'),
        ('telecommunications specialist', 'Telecommunications Specialist'),
        ('VR/AR developer', 'VR/AR Developer'),
        ('blockchain developer', 'Blockchain Developer'),
        ('other', 'Other')
        # 其他職業選項
    )
    # 其他欄位
    occupation = models.CharField(max_length=100, choices=OCCUPATION_CHOICES, blank=True, null=True)  # 職業欄位，最大長度為 100，選項限定在 OCCUPATION_CHOICES 中
    academic = models.CharField(max_length=100, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user_id
