from django.core import paginator
from django.db import connection, models
from django.http import request
from django.shortcuts import get_object_or_404, redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView
from django.core.paginator import Paginator
from . import models


def intro(request):
    return render(request, "posts/intro.html")


class Homeview(ListView):

    model = models.Post
    template_name = "posts/home.html"


def CategoryView(request, category_name):
    page = request.GET.get("page")
    category_posts = models.Post.objects.filter(category=category_name)
    paginator = Paginator(category_posts, 10)
    posts = paginator.get_page(page)
    categories = models.Category.objects.all()
    return render(
        request,
        "posts/categories.html",
        {
            "category_name": category_name,
            "category_posts": category_posts,
            "categories": categories,
            "posts": posts,
        },
    )


class PostDetailView(DetailView):

    model = models.Post
    template_name = "posts/post_detail.html"


class DeletePostView(DeleteView):

    model = models.Post
    template_name = "auth/confirm_delete.html"
    success_url = reverse_lazy("posts:list")
