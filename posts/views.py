from django.db import models
from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class Homeview(ListView):

    model = models.Post
    template_name = "posts/home.html"
