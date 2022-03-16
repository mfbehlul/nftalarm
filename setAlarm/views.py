from django.shortcuts import render

# Create your views here.

def set_alarm_view(request):
    text=request.GET
    

    context={}
    return render(request,"setAlarm.html",context)
