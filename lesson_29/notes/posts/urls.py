from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListCreateAPIView.as_view(), name="post_list_create"),
    path(
        "<str:pk>", views.PostRetrieveUpdateDestroyAPIView.as_view(), name="post_detail"
    ),
    path("tags/", views.TagListCreateAPIView.as_view(), name="tag_list_create"),
]
