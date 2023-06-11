from django.shortcuts import render, redirect
from .models import Category, Question, Quiz, QuizResult, QuizResultDetail
from .filters import CategoryFilter, QuestionFilter, QuizFilter, QuizResultFilter
from .forms import CategoryForm, QuestionForm, QuizForm
import random
import json

# Create your views here.
def question(request):
    quiz_id = request.GET.get('quizid')
    quiz = Quiz.objects.get(id=quiz_id)    
    questions = []
    for question in quiz.quiz_questions.all():
        questions.append(question)
    return render(request, 'quiz/quiz.html', locals())

def quizindex(request):
    return render(request, 'quiz/quizindex.html')

def quizresult(request):
    if request.method == 'POST':
        quiz_result = None
        quiz = None
        questions = []
        userAnswer = []
        correct_amount = 0
        user_answer_time = 0
        # 獲取表單數據
        for i, (key, value) in enumerate(request.POST.items()):
            # csrfmiddlewaretoken 為 CSRF 驗證所需的隱藏欄位，不需要處理
            if i == 0:
                pass
            # quiz_id
            elif i == 1:
                quiz_id = value
                # 保存 QuizResult 物件
                quiz = Quiz.objects.get(id=quiz_id)
                quiz_result = QuizResult.objects.create(
                    quiz=quiz,
                    user_id=request.user.id,
                    score=100,
                    user_answer_time=0,
                )
            elif i == 2:
                user_answer_time = value
                quiz_result.user_answer_time = user_answer_time
                quiz_result.save()
            else:
                question_dict = json.loads(value)  # 將 JSON 字串轉換為字典
                question_id = question_dict.get('id')  # 獲取題目 ID
                user_answer = question_dict.get('userAnswer')  # 獲取用戶的答案
                question = Question.objects.get(id=question_id)
                questions.append(question)
                userAnswer.append(user_answer)
                correct = False

                #答對
                if question.correct_answer == user_answer:
                    correct_amount += 1
                    correct = True
                
                if user_answer == 'A':
                    question.choice1_selected += 1
                elif user_answer == 'B':
                    question.choice2_selected += 1
                elif user_answer == 'C':
                    question.choice3_selected += 1
                elif user_answer == 'D':
                    question.choice4_selected += 1
                question.save()

                # 保存 QuizResultDetail 物件
                quiz_result_detail = QuizResultDetail.objects.create(
                    quiz_result=quiz_result,
                    question=question,
                    user_answer=user_answer,
                    correct=correct
                )
                # print(i, question_id, question_dict.get('userAnswer'))
        quiz_result.score = correct_amount * quiz.question_score
        quiz_result.correct_amount = correct_amount
        quiz_result.save() 

    return render(request, 'quiz/quizresult.html', locals())

def quiz_admin(request):
    questionForm = QuestionForm()
    quizForm = QuizForm()
    categoryForm = CategoryForm()
    questions = Question.objects.all()
    selected_questions = []
    current_tab = 0
    if request.method == "POST":
        print(request.POST)
        if 'queryForm' in request.POST:
            questionFilter = QuestionFilter(request.POST, queryset=questions)
            if questionFilter.is_valid():
                print(request.POST.getlist('selected_questions'))
                if request.POST.get('selected_questions') == '' or request.POST.getlist('selected_questions')[0] == '[]':
                    selected_questions = []
                else:
                    selected_questions = list(map(int, request.POST.getlist('selected_questions')[0].replace('[', '').replace(']', '').split(',')))
                # print(selected_questions)
                # print(request.POST['quiz_name'])
                questions = questionFilter.qs
                # quizForm = QuizForm({'quiz_name': request.POST['quiz_name'], 'quiz_description': request.POST['quiz_description']})
                current_tab = 'three'
        elif 'categoryForm' in request.POST:
            categoryForm = CategoryForm(request.POST)
            if categoryForm.is_valid():
                category = categoryForm.save()
                return redirect('quiz_admin')
            else:
                current_tab = 'one'
            
        elif 'questionForm' in request.POST:
            questionForm = QuestionForm(request.POST)
            if questionForm.is_valid():
                question = questionForm.save()
                question.category.set(questionForm.cleaned_data.get('category'))
                current_tab = 'two'
                return redirect('quiz_admin')
        elif 'quizForm' in request.POST:
            quizForm = QuizForm(request.POST)
            if quizForm.is_valid():
                quiz = quizForm.save()
                current_tab = 'three'
                return redirect('quiz_admin')
    else:
        # Get request, no form submission
        questionFilter = QuestionFilter(queryset=questions)
        
    # categories = Category.objects.all()
    # questions = Question.objects.all()
    # quizzes = Quiz.objects.all()
    # quiz_results = QuizResult.objects.all()

    # categoryFilter = CategoryFilter(queryset=categories)
    # questionFilter = QuestionFilter(queryset=questions)
    # quizFilter = QuizFilter(queryset=quizzes)
    # quizResultFilter = QuizResultFilter(queryset=quiz_results)
    # if request.method == "POST":
    #     categoryFilter = CategoryFilter(request.POST, queryset=categories)
    #     questionFilter = QuestionFilter(request.POST, queryset=questions)
    #     quizFilter = QuizFilter(request.POST, queryset=quizzes)
    #     quizResultFilter = QuizResultFilter(request.POST, queryset=quiz_results)
        
    return render(request, 'quiz/quizadmin.html', locals())