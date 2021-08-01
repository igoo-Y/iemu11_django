from django.db import models
from django.urls import reverse
from core import models as core_models
from users import models as user_models


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home")


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    category = models.CharField(max_length=30, default="공지사항")
    title = models.CharField(max_length=80)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title[:20]
