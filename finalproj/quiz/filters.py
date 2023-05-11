from .models import Question, Quiz, QuizResult, QuizResultDetail
import django_filters

class QuestionFilter(django_filters.FilterSet):
 
    class Meta:
        model = Question
        fields = '__all__'