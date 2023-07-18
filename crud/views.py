from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Blog #manager objects
# Create your views here.

def index(request):
    blog = Blog.objects.all()
    print(blog)
    return render(request, "crud/index.html",{"blogs":blog})

def about(request):
    return render(request, "crud/about.html")
