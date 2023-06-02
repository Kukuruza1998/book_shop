from django.shortcuts import render
from django.views import generic

#Homepage

class HomePage(generic.TemplateView):
    template_name = "homepage/home-page.html"
