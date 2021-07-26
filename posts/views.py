from django.db import models
from django.http import request
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.urls import reverse_lazy
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


class PostDetailView(DetailView):

    model = models.Post
    template_name = "posts/post_detail.html"


class DeletePostView(DeleteView):

    model = models.Post
    template_name = "auth/confirm_delete.html"
    success_url = reverse_lazy("posts:list")
