from .models import Tag, Question, Quiz, QuizResult, QuizResultDetail
import django_filters

class TagFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(lookup_expr='icontains', label='Category')

    class Meta:
        model = Tag
        fields = ['tag']

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