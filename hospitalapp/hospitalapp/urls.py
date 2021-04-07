"""hospitalapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from hospital.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('view_doctor/',View_Doctor,name='view_doctor'),
    path('view_patient/',View_Patient,name='view_patient'),
    path('view_appiontment/',View_Appiontment,name='view_appiontment'),
    path('add_doctor/',Add_Doctor,name='add_doctor'),
    path('add_patient/',Add_Patient,name='add_patient'),
    path('add_appiontment/',Add_Appiontment,name='add_appiontment'),
    path('',Index,name='home'),
    path('admin_login',Login,name='login'),
    path('logout/',Logout,name='logout'),
    path('delete_doctor(?p<int:pid>)',Delete_Doctor,name='delete_doctor'),
    path('delete_patient(?p<int:pid>)',Delete_Patient,name='delete_patient'),
    path('delete_appiontment(?p<int:pid>)',Delete_Appiotnment,name='delete_appiontment')

]
