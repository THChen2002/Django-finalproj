from django import template

register = template.Library()

@register.filter
def get_answer(userAnswer, index):
    print(index, userAnswer[index-1])
    return userAnswer[index-1]