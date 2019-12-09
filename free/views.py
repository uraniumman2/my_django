from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer

from .models import Task


def home_page(request):
    return render(request, "hello_world.html", {"title": "gg", "list_t": [1, 34, 5, 2, 3, 45]})


@api_view(['GET', 'PUT', 'DELETE'])
def blog_post_detail_api(request, pk):
    """
    Get, update or delete specific blog post
    :param request:
    :param pk:
    :return:
    """
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def blog_post_api(request):
    """
    List of all BlogPosts
    :param request:
    :return:
    """
    if request.method == 'GET':
        tasks = Task.objects.all()
        for task in tasks:
            print(task.title)
        serializer = TaskSerializer(tasks, many=True)
        print(tasks)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def about_page(request):
    return HttpResponse("<h1>About</h1>")


def contact_page(request):
    return HttpResponse("<h1>Contact</h1>")


def example_page(request):
    context = {"title": "Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    return HttpResponse(template_obj.render(context))
