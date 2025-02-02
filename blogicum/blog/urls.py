from django.urls import path
from . import views


app_name = "blog"

url_c = "category/<slug:category_slug>/"

urlpatterns = [
    path("", views.index, name="index"),
    path("posts/<int:id>/", views.post_detail, name="post_detail"),
    path(url_c, views.category_posts, name="category_posts")
]
