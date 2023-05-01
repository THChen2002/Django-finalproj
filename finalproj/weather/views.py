from django.shortcuts import render,redirect

# Create your views here.

def weather(request):
    return render(request, 'weather/weather.html')

def town(request):
    tid = request.GET.get('TID')
    if tid:
        url = f'/weather/town?TID={tid}'
        # return redirect(url)
    else:
        pass
    return render(request, 'weather/town.html', locals())

def radar(request):
    return render(request, 'weather/radar.html')
