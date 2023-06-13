from django.contrib import admin
from .models import Question, Tag, Quiz, QuizResult, QuizResultDetail

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'question_type', 'question_level', 'correct_amount', 'total_amount')
    filter_horizontal = ('tag',)
    list_filter = ["tag"]

class QuizAdmin(admin.ModelAdmin):
    list_display = ('quiz_name', 'question_amount', 'question_score', 'quiz_time')
    filter_horizontal = ('quiz_questions',)

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'score')

class QuizResultDetailAdmin(admin.ModelAdmin):
    list_display = ('quiz_result', 'question', 'correct')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Tag)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
admin.site.register(QuizResultDetail, QuizResultDetailAdmin)