from django.urls import path

from . import views

urlpatterns = [
    path("category/", views.category, name="category"),
    path("category/edit/<int:id>", views.edit_category, name="edit_category"),
    path("category/delete/<int:id>", views.delete_category, name="delete_category"),
    path("category/create", views.CreateCategory.as_view(), name="create_category"),
    path("users/", views.FDUserListView.as_view(), name="users"),
    path("users/edit/<int:id>", views.EditFDUser.as_view(), name="edit_user"),
    path("users/delete/<int:id>", views.delete_user, name="delete_user"),
    path("users/create_user/", views.CreateFDUser.as_view(), name="create_user"),
    path("", views.FoodListView.as_view(), name="food"),
    path("edit/<int:id>", views.EditFood.as_view(), name="edit_food"),
    path("create/", views.CreateFood.as_view(), name="create_food"),
    path("delete/<int:id>", views.delete_food, name="delete_food"),
]
