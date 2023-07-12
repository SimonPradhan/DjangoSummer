from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. How are you guys? :)")
