from django.shortcuts import render
from django.http import HttpResponse
from .models import post

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    posts = post.objects.all()
    return render(request, 'blog.html', {'posts': posts})


