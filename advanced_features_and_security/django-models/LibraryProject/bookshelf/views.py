from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import UpdateView
from .models import CustomUser
from django.contrib.auth.decorators import permission_required
def index(request):
    return HttpResponse("Welcome to the Bookshelf App!")

# Create your views here.

@permission_required("bookshelf.can_edit",raise_exception = True)
def edit_post(request,post_id):
    return render (request,'edit_post.html')

class PostUpdateView(PermissionRequiredMixin,UpdateView):
    model = CustomUser
    fields = ["title", "content"]
    template_name = "edit_post.html"
    permission_required = "blog.can_edit"
    raise_exception = True