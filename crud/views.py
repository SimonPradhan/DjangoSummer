from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Blog, Contacts #manager objects
from .forms import BlogForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    blog = Blog.objects.all()
    print(blog)
    return render(request, "crud/home.html",{"blogs":blog})

def about(request):
    return render(request, "crud/about.html")

def create(request):
    form= BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "crud/create.html", {"form":form})

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("index")

def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("index")
    return render(request, "crud/create.html", {"form":form, "blog":blog})

def partData(request, id):
    blog = Blog.objects.get(id=id)
    context ={
        "blog":blog
    }
    return render(request, "crud/index.html", context)

def contacts(request):
    if(request.method == 'POST'):
        dataName= request.POST.get("name")
        dataEmail= request.POST.get("email")
        
        contacts= Contacts(
            name = dataName,
            email=dataEmail
        )
        contacts.save()
    return render(request, "crud\contactus.html")

