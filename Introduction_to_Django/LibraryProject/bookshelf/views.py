from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return HttpResponse("Welcome to the Bookshelf App!")

# Create your views here.
