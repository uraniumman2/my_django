from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template

from .models import BlogPost

def home_page(request):
    return render(request, "hello_world.html", {"title": "gg", "list_t":[1,34,5,2,3,45]})


def blog_post_detail_page(request, slug):
    obj = get_object_or_404(BlogPost, slug = slug)
    return render(request,"blog_post_detail.html", {"object":obj})

def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
