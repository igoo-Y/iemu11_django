from django.db import models
from core import models as core_models
from users import models as user_models


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    name = models.CharField(max_length=20)


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    title = models.CharField(max_length=80)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    body = models.TextField()
