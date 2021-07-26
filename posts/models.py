from django.db import models
from core import models as core_models
from users import models as user_models


class Category(core_models.TimeStampedModel):

    """Category Model Definition"""

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Post(core_models.TimeStampedModel):

    """Post Model Definition"""

    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=80)
    writer = models.ForeignKey(user_models.User, on_delete=models.CASCADE, null=True)
    body = models.TextField()

    def __str__(self):
        return self.title[:20]
