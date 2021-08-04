from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("<int:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("<int:pk>/delete/", views.DeletePostView.as_view(), name="delete"),
    path("category/<str:category_name>/", views.CategoryView, name="category"),
]
