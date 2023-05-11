from django.contrib import admin
from .models import Question, Category, Quiz, QuizResult, QuizResultDetail

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'question_level', 'correct_answer')
    filter_horizontal = ('category',)
    list_filter = ["category"]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_name', 'question_amount', 'question_score', 'quiz_time')
    filter_horizontal = ('quiz_questions',)

admin.site.register(Question, QuestionAdmin)
admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult)
admin.site.register(QuizResultDetail)