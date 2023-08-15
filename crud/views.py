from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Blog, Contacts, Footer #manager objects
from .forms import BlogForm
from django.shortcuts import redirect

from django.core.paginator import Paginator

# email
from firstProject.settings import EMAIL_HOST_USER
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from django.contrib.auth.decorators import login_required


# Create your views here.

footer = Footer.objects.all()
def index(request):
    blog = Blog.objects.all()
    paginator = Paginator(blog, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "blogs":page_obj,
        "footer":footer
        }
    search_data = request.GET.get('search')
    if search_data != "" and search_data is not None:
        data = Blog.objects.filter(title__icontains=search_data)
        paginator = Paginator(data, 2)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            "blogs":page_obj,
            "footer":footer,
            }
        return render(request, "crud/home.html", context)
    return render(request, "crud/home.html", context)

def about(request):
    return render(request, "crud/about.html")

@login_required
def create(request):
    form= BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("crud:index")
    return render(request, "crud/createblog.html", {"form":form})

def delete(request, id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect("crud:index")

def update(request, id):
    blog = Blog.objects.get(id=id)
    form = BlogForm(request.POST or None, instance=blog)
    if form.is_valid():
        form.save()
        return redirect("crud:index")
    return render(request, "crud/createblog.html", {"form":form, "blog":blog})

def partData(request, id):
    blog = Blog.objects.get(id=id)
    context ={
        "blog":blog
    }
    return render(request, "crud/post.html", context)

def contacts(request):
    if(request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        contact = Contacts(name=name, email=email)
        subject = "Welcome to Blog Application"
        recipient = [email]
        contact.save()
        template = render_to_string('migrations/email.html',{'name':name,'description':message,'mail':email})
        email=EmailMessage(
               subject,
               template,
               EMAIL_HOST_USER,
               recipient
           )
        email.fail_silently=False
        if email!=None:
            email.send()
    return render(request, "crud\contact.html", {"footer":footer})

def post(request):
    return render(request, "crud/post.html")

def signup(request):
    return render(request, "crud/signup.html")

def login(request):
    return render(request, "crud/login.html")

# def footer(request):
#     footer = Footer.objects.all()
#     context = {
#         "footer":footer
#     }
#     return render(request, "crud/home.html", context)
