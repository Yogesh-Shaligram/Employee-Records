"""emp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from task .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #API-1
    url('api/firsttask', firsttask),
    #API-2
    url('api/secondtask', secondtask),
    # API-3
    url('api/thirdtask', thirdtask),
    # API-4
    url('api/fourthtask', fourthtask),
    # API-5
    url('api/fifthtask', fifthtask),
    # API-6
    url('api/sixthtask', sixthtask),
]