from django import forms
from .models import Category, Question, Quiz

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'question_url', 'category', 'choice1', 'choice2', 'choice3', 'choice4', 'question_type', 'question_level', 'correct_answer', 'detail_explanation', 'explanation_url']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
