from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryModelAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Post)
class PostModelAdmin(admin.ModelAdmin):

    """Post Model Admin Definition"""

    list_display = (
        "category",
        "writer",
        "title",
    )

    list_filter = ("category",)
