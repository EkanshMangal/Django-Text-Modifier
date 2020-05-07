# This file is made by me

from django.http import HttpResponse

def index(request):
    return HttpResponse("hello ekansh How are you???")

def about(request):
    return HttpResponse("<h1> About me </h1>")      