from django.shortcuts import render,redirect

# Create your views here.

def weather(request):
    return render(request, 'weather/weather.html')

def town(request):
    print(request.GET)
    tid = request.GET.get('TID')
    print(tid)
    if tid:
        url = f'/weather/town?TID={tid}'
        # return redirect(url)
    else:
        url = '/weather/town?TID=6300200'
        return redirect(url)
    return render(request, 'weather/town.html', locals())

def radar(request):
    return render(request, 'weather/radar.html')
