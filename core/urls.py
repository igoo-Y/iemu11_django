from django.urls import path
from posts import views as post_views

app_name = "core"

urlpatterns = [
    path("", post_views.Homeview.as_view(), name="home"),
    path("intro", post_views.intro, name="intro"),
]
