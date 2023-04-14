from django.shortcuts import render

# Create your views here.

#blog頁面
def blog(request):
    return render(request, 'blog/blog.html')