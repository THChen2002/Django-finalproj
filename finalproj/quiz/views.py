from django.shortcuts import render
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
    quiz = Quiz.objects.get(id=1)    
    questions = []
    for question in quiz.quiz_questions.all():
        questions.append(question)
    return render(request, 'quiz/quiz.html', locals())

def quizindex(request):
    return render(request, 'quiz/quizindex.html')

def quizresult(request):
    if request.method == 'POST':
        questions = []
        userAnswer = []
        for i, (key, value) in enumerate(request.POST.items()):
            if i == 0:
                pass
            else:
                question_dict = json.loads(value)  # 将字符串解析为字典
                question_id = question_dict.get('id')  # 获取字典中的id值
                questions.append(Question.objects.get(id=question_id))
                userAnswer.append(question_dict.get('userAnswer'))
                # print(i, question_id, question_dict.get('userAnswer'))
        # 獲取表單數據
    #     quiz_id = request.POST.get('quiz_id')
    #     user_id = request.POST.get('user_id')
    #     score = request.POST.get('score')
    #     answers = request.POST.getlist('answers')  # 假設答案以列表形式提交
        
    #     # 保存 QuizResult 物件
    #     quiz_result = QuizResult.objects.create(
    #         quiz_id=quiz_id,
    #         user_id=user_id,
    #         score=score
    #     )
        
    #     # 保存 QuizResultDetail 物件
    #     for i, answer in enumerate(answers):
    #         question_id = request.POST.get(f'question_{i}_id')  # 假設每個問題的ID為 question_<i>_id
    #         user_answer = answer
    #         # 根據需要進行其他欄位的獲取
            
    #         quiz_result_detail = QuizResultDetail.objects.create(
    #             quiz_result=quiz_result,
    #             question_id=question_id,
    #             user_answer=user_answer
    #             # 根據需要進行其他欄位的賦值
    #         )
        
    #     return redirect('quiz_results')  # 重新導向到顯示測驗結果的頁面
    
    # 如果不是 POST 請求，可能需要進行其他處理，例如渲染提交頁面
    return render(request, 'quiz/quizresult.html', locals())