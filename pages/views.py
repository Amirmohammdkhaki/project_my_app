from django.shortcuts import render
from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name='home.html'


class About(TemplateView):
    template_name='pages/about.html'


