from django.urls import path

from . import views

urlpatterns = [
    path("category/", views.category, name="category"),
    path("category/edit/<int:id>", views.edit_category, name="edit_category"),
]
