from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from . import models


def intro(request):
    return render(request, "posts/intro.html")


class Homeview(ListView):

    model = models.Post
    template_name = "posts/home.html"


class PostListView(ListView):
    model = models.Post
    template_name = "posts/posts_list.html"
    context_object_name = "posts"
