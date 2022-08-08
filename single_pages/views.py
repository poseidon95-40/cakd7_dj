from django.shortcuts import render
from requests import request
from django.views.generic import ListView, DetailView
#from .models import Post
#from .models import Post

# Create your views here.

# class Landing():
#     template_name =  'single_pages/landing.html'

# class About_me():
#      template_name =  'single_pages/about_me.html'
     
def landing(request):
    return render(request, 'single_pages/landing.html')
    
def about_me(request):
    return render(request, 'single_pages/about_me.html')
