"""nftalarmcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from setAlarm.views import set_alarm_view, load_attributes,show_results,active_alarms
from accounts.views import login_view,register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('set-alarm/',set_alarm_view,name="setAlarm"),
    path('attributes/',load_attributes,name="loadAttributes"),
    path('login/', login_view, name="login"),
    path('logout/', login_view, name="logout"),
    path('register/', register_view, name="register"),
    path('results/',show_results,name="results"),
    path('active-alarms/',active_alarms,name="activeAlarms"),

]
