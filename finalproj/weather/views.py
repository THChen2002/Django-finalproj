from django.shortcuts import render

# Create your views here.

def weather(request):
    return render(request, 'weather/weather.html')

def radar(request):
    return render(request, 'weather/radar.html')
