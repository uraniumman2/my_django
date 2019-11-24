from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template


def home_page(request):
    title = "HELLO MFKA"
    return render(request, "hello_world.html", {"title": title})


def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
