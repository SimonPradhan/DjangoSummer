from django.http import HttpResponse

def index(request):
    return HttpResponse("Oh Hello, world. How are you guys? :)")


