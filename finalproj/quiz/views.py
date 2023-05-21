from django.shortcuts import render, redirect
from .models import Question, Quiz, QuizResult, QuizResultDetail
import random
import json

# Create your views here.
def question(request):
    # questions_length = len(Question.objects.all())
    # questions_order = random.sample(range(1, questions_length+1), questions_length)
    # questions = []
    # for id in questions_order:
    #     question = Question.objects.get(id=id)
    #     questions.append(question)
    quiz_id = 1
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