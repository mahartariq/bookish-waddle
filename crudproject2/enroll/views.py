from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from .forms import StudentRegistration
from .models import User
from django.views.generic.base import TemplateView
# Create your views here.

class Add_Show(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistration()
        std = User.objects.all()
        context = {'forms':fm,'stu':std}
        return context
    def post(self,request):
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            cname = fm.cleaned_data['name']
            cpassword = fm.cleaned_data['password']
            cemail = fm.cleaned_data['email']
            reg = User(name=cname,password=cpassword,email=cemail)
            reg.save()
            return HttpResponseRedirect('/')



class Update_Data(View):
    def get(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)    
        return render(request,'enroll/updatestudent.html',{'form':fm})
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/')




'''
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
'''

from django.views.generic.base import RedirectView
class Delete_Data(RedirectView):

    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()

        return super().get_redirect_url(*args, **kwargs)

'''
def delete_data(request,id):
    if request.method == 'POST':    
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')
        '''
