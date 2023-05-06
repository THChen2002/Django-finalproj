from django.contrib import admin
from .models import Question, Category, Quiz, QuizResult, QuizResultDetail

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'question_level', 'correct_answer')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Quiz)
admin.site.register(QuizResult)
admin.site.register(QuizResultDetail)