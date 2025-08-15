from django.urls import path
from django.shortcuts import render

def blog_view(request):
    return render(request, 'blog.html')

def about_view(request):
    return render(request, 'about.html')

urlpatterns = [
    path('', blog_view, name='blog'),  # /blog/
    path('about/', about_view, name='about'),  # /blog/about/
]
