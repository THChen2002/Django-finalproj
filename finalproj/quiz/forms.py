from django import forms
from .models import Category, Question, Quiz

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        widgets = {
            'category': forms.TextInput(attrs={'class': 'form-control'}),
        }
        fields = '__all__'

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question', 'question_url', 'category', 'choice1', 'choice2', 'choice3', 'choice4', 'question_type', 'question_level', 'correct_answer', 'detail_explanation', 'explanation_url']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control'}),
            'question_url': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'choice1': forms.TextInput(attrs={'class': 'form-control'}),
            'choice2': forms.TextInput(attrs={'class': 'form-control'}),
            'choice3': forms.TextInput(attrs={'class': 'form-control'}),
            'choice4': forms.TextInput(attrs={'class': 'form-control'}),
            'question_type': forms.Select(attrs={'class': 'form-control'}),
            'question_level': forms.NumberInput(attrs={'class': 'form-control'}),
            'correct_answer': forms.Select(attrs={'class': 'form-control'}),
            'detail_explanation': forms.Textarea(attrs={'class': 'form-control'}),
            'explanation_url': forms.TextInput(attrs={'class': 'form-control'}),
        }

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = '__all__'
        widgets = {
            'quiz_name': forms.TextInput(attrs={'class': 'form-control'}),
            'quiz_description': forms.Textarea(attrs={'class': 'form-control'}),
            'quiz_questions': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'question_amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'question_score': forms.NumberInput(attrs={'class': 'form-control'}),
            'quiz_time': forms.NumberInput(attrs={'class': 'form-control'}),
        }