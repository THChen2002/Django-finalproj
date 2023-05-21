from django import template

register = template.Library()

@register.filter
def get_answer(userAnswer, index):
    # print(index, userAnswer[index-1])
    return userAnswer[index-1]

@register.filter
def get_str_time(user_answer_time):
    user_answer_time = int(user_answer_time)
    minutes = user_answer_time // 60
    seconds = user_answer_time % 60
    time_str = f"{minutes:02d}:{seconds:02d}"
    return time_str

@register.filter
def times(number):
    return range(number)