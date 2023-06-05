from django import template

register = template.Library()

@register.filter
def rangetag(start, end):
    return range(start, end+1)

@register.filter
def page_range(currentpage, totpage):
    start = max(currentpage - 2, 1)
    end = min(currentpage + 2, totpage)
    return range(start, end+1)

@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def add(value, arg):
    value = int(value)
    return value + arg