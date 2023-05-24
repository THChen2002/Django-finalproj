from .models import Category, Question, Quiz, QuizResult, QuizResultDetail
import django_filters

class CategoryFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='icontains', label='Category')

    class Meta:
        model = Category
        fields = ['category']

class QuestionFilter(django_filters.FilterSet):
    question = django_filters.CharFilter(lookup_expr='icontains', label='Question')

    class Meta:
        model = Question
        fields = '__all__'

class QuizFilter(django_filters.FilterSet):
    quiz_name = django_filters.CharFilter(lookup_expr='icontains', label='Quiz Name')

    class Meta:
        model = Quiz
        fields = '__all__'

class QuizResultFilter(django_filters.FilterSet):
    quiz = django_filters.CharFilter(lookup_expr='icontains', label='Quiz')
    user = django_filters.CharFilter(lookup_expr='icontains', label='User')

    class Meta:
        model = QuizResult
        fields = '__all__'