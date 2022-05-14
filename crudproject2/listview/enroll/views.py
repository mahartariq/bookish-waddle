from django.shortcuts import render
from django.views.generic.detail import DetailView
# Create your views here.
from .models import Student
from django.views.generic.list import ListView


class StudentDetailedView(DetailView):
    model = Student

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
#        context['all_data'] = self.model.objects.all()
        context['all_data'] = Student.objects.all()
        return context

class StudentListView(ListView):
    model = Student    