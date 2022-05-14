from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            cname = fm.cleaned_data['name']
            cpassword = fm.cleaned_data['password']
            cemail = fm.cleaned_data['email']
            reg = User(name=cname,password=cpassword,email=cemail)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    std = User.objects.all()
    return render(request,'enroll/addandshow.html',{'forms':fm,'stu':std})

def update_data(request,id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
            #cname = fm.cleaned_data['name']
            #cemail = fm.cleaned_data['email']
            #cpassword = fm.cleaned_data['password']
            #reg = User(pk=id,name=cname,password=cpassword,email=cemail)
            #reg.save()
            #fm = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)    
    return render(request,'enroll/updatestudent.html',{'form':fm})


def delete_data(request,id):
    if request.method == 'POST':    
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')