from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login


def About(request):
    return render(request,'about.html')

def Add_Doctor(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        n = request.POST['name']
        p = request.POST['contact']
        s = request.POST['special']
        try:
            Doctor.objects.create(name=n,mobile=p,special=s)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_doctor.html',d)
def Add_Patient(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        k = request.POST['name1']
        l = request.POST['contact1']
        e = request.POST['gender']
        d = request.POST['address']
        try:
            Patient.objects.create(name=k,mobile=l,gender=e,address=d)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_patient.html',d)
def Add_Appiontment(request):
    error=""
    if not request.user.is_staff:
        return redirect('login')
    if request.method=='POST':
        f = request.POST['name3']
        t = request.POST['name4']
        v = request.POST['name5']
        q = request.POST['date']
        z = request.POST['time']
        try:
            Doctor.objects.create(doctor=f,patient=t,name=v,date1=q,time1=z)
            error="no"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'add_appiontment.html',d)
def Navigation(request):
    return render(request,'navigation.html')
def Contact(request):
    return render(request,'contact.html')
def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Doctor.objects.all()
    d={'doc':doc}
    return render(request,'view_doctor.html',d)
def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Patient.objects.all()
    d={'doc':doc}
    return render(request,'view_patient.html',d)
def View_Appiontment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc=Appointment.objects.all()
    d={'doc':doc}
    return render(request,'view_appiontment.html',d)
def Login(request):
    error=""
    if request.method=='POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request,User)
                error="no"
            else:
                error="yes"
        except:
            error="yes"
    d = {'error':error}
    return render(request,'login.html',d)
def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    return render(request,'index.html')
def Logout(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('login')
def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirct('login')
    doctor=Doctor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')



# Create your views here.
