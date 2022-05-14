from re import template
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView

from .forms import ContactForm

class ContactFormView(FormView):
    template_name = 'depart/contact.html'
    form_class = ContactForm
    success_url = '/thankyou/'

    def form_valid(self, form):
        return HttpResponse('DOneneh')


class ThankYouView(TemplateView):
    template_name = 'depart/thanks.html'