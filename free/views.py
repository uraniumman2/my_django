from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home_page(request):
    title = "HELLO MFKA"
    return render(request, "hello_world.html", {"title": title})


def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")
