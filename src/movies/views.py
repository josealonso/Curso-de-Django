from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def hello_world(request):
    #  name = request.GET["name"]
    name = request.GET.get("name")
    if name is None:
        return HttpResponse("Hello world !!")
    else:
        return HttpResponse("Hello " + name)
