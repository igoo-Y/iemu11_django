from django.db import connection, models
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
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


def posts_in_category(request, category_pk=None):
    categories = models.Category.objects.all()
    category_pk = request.get("category.pk")
    posts = models.Post.objects.all()
    if category_pk:
        current_category = get_object_or_404(models.Category, category_pk=category_pk)
        posts = models.Post.objects.filter(category=category_pk)
    context = {
        "categories": categories,
        "current_category": current_category,
        "posts": post,
    }
    return render(request, "posts/posts_list.html", context=context)
