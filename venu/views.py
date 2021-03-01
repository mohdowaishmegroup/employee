from django.shortcuts import render
from venu.models import Empinsert
from django.contrib import messages


def InsertRecord(request):
    if request.method=='POST':
        if request.POST.get('empname') and request.POST.get('email')and request.POST.get('country'):
            saverecord=Empinsert()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.country=request.POST.get('email')
            saverecord.save()
            messages.success(request,"record sucessfully saved")
            return render(request,'index.html')
    else:
        return render(request, 'index.html')
