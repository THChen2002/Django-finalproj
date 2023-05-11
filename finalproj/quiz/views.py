from django.shortcuts import render
from .models import Question, Quiz, QuizResult, QuizResultDetail
import random

# Create your views here.
def question(request):
    questions_length = len(Question.objects.all())
    questions_order = random.sample(range(1, questions_length+1), questions_length)
    questions = []
    for id in questions_order:
        question = Question.objects.get(id=id)
        questions.append(question)
    return render(request, 'quiz/quiz.html', locals())