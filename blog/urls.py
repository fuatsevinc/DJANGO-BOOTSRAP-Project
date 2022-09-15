from django.urls import path
from .views import post_list, post_create, post_detail, post_update, post_delete, like

app_name = "blog"
urlpatterns = [
    path("blog/",post_list, name="list"),
    path("blog/<str:slug>/",post_detail, name="detail"),
    path("blog/<create/",post_create, name="create"),
    path("blog/<str:slug>/update/",post_update, name="update"),
    path("blog/<str:slug>/delete/",post_delete, name="delete"),
    path("blog/<str:slug>/like/",like, name="like"),
]