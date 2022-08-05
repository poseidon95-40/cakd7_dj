from django.shortcuts import render
#from django.views.generic import ListView, DetailView
#from .models import Post

# Create your views here.

# class Landing(ListView):
#     model = Post
#     ordering = '-pk'
#     template_name =  'single_pages/landing.html'

# class About_Me(DetailView):
#     model = Post    


def landing(request):
    return render(request, 'single_pages/landing.html')
    
def about_me(request):
    return render(request, 'single_pages/about_me.html')
