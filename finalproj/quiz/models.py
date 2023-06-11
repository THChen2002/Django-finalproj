from django.db import models
from accounts.models import UserProfile
from blog.models import BlogPost

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.category

class Question(models.Model):
    question = models.CharField(max_length=500, blank=False)
    # question_url = models.ImageField(upload_to='question_pics/',blank=True, null=True)
    question_url = models.URLField(blank=True, null=True)
    category = models.ManyToManyField(Category)
    choice1 = models.CharField(max_length=150)
    choice2 = models.CharField(max_length=150)
    choice3 = models.CharField(max_length=150)
    choice4 = models.CharField(max_length=150)
    TYPE_CHOICES = (
        ('Multiple Choice', 'Multiple Choice'),
        ('True or False', 'True or False'),
    )
    question_type = models.CharField(max_length=50,choices= TYPE_CHOICES)
    question_level = models.IntegerField(blank=False)
    correct_answer = models.CharField(max_length=50, choices=(
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
    ))
    # blog = models.ForeignKey(BlogPost, on_delete=models.CASCADE, blank=True,null=True)
    detail_explanation = models.TextField(blank=True, null=True)
    # explanation_url = models.ImageField(upload_to='explanation_pics/',blank=True, null=True)
    explanation_url = models.URLField(blank=True, null=True)
    choice1_selected = models.IntegerField(default=0)
    choice2_selected = models.IntegerField(default=0)
    choice3_selected = models.IntegerField(default=0)
    choice4_selected = models.IntegerField(default=0)
    total_amount = models.IntegerField(default=0)
    correct_amount = models.IntegerField(default=0)
    correct_rate = models.FloatField(default=0)
    def __str__(self):
        return self.question
    
    def save(self, *args, **kwargs):
        if self.correct_answer == 'A':
            self.correct_amount = self.choice1_selected
        elif self.correct_answer == 'B':
            self.correct_amount = self.choice2_selected
        elif self.correct_answer == 'C':
            self.correct_amount = self.choice3_selected
        elif self.correct_answer == 'D':
            self.correct_amount = self.choice4_selected

        self.total_amount = self.choice1_selected + self.choice2_selected + self.choice3_selected + self.choice4_selected
        if self.total_amount > 0:
            self.correct_rate = round((self.correct_amount / self.total_amount), 4)*100
        super().save(*args, **kwargs)


class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50)
    quiz_description = models.TextField(blank=True, null=True)
    quiz_questions = models.ManyToManyField(Question)
    question_amount = models.IntegerField(blank=False, default=10)
    question_score = models.IntegerField(blank=False, default=10)
    quiz_time = models.IntegerField(blank=False, default=300)
    def __str__(self):
        return self.quiz_name
    
    def save(self, *args, **kwargs):
        if self.question_amount > 0:
            self.question_score = 100 / self.question_amount
        super().save(*args, **kwargs)

class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.PROTECT)
    user = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    correct_amount = models.IntegerField(blank=False,default=0)
    score = models.IntegerField(blank=False)
    user_answer_time = models.IntegerField(blank=False, default=0)
    def __str__(self):
        return self.quiz.quiz_name + ' - ' + self.user.user.username + ' - ' + str(self.score)
    
class QuizResultDetail(models.Model):
    quiz_result = models.ForeignKey(QuizResult, on_delete=models.PROTECT)
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    user_answer = models.CharField(max_length=50)
    correct = models.BooleanField(default=False)
    def __str__(self):
        return self.quiz_result.quiz.quiz_name