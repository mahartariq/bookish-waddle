from django.shortcuts import render
from .models import Student
# Create your views here.
from django.views.generic.list import ListView

class StudentListView(ListView):
    model = Student
    #template_name_suffix = '_get'
    template_name = 'portal/student.html'
    context_object_name = 'students'

    def get_queryset(self):
        return Student.objects.filter(course_name = 'Cloud Native Computing')

    def get_context_data(self,*args, **kwargs):
        context = super().get_context_data(*args,**kwargs)
        context['Freshers']  = Student.objects.all().order_by('name')
        return context