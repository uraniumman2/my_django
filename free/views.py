from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.http import Http404

from .models import BlogPost

def home_page(request):
    return render(request, "hello_world.html", {"title": "gg", "list_t":[1,34,5,2,3,45]})


def blog_post_detail_page(request, idx):
    try:
        obj = BlogPost.objects.get(id = idx)
    except BlogPost.DoesNotExist:
        raise Http404
    except ValueError:
        raise Http404
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
