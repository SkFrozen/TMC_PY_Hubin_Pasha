from django.forms import ModelForm

from .models import Category, FDUser, Food


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class EditUserForm(ModelForm):
    class Meta:
        model = FDUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
        ]


class CreateUserForm(ModelForm):
    class Meta:
        model = FDUser
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "role",
            "password",
        ]


class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = [
            "name",
            "cost",
            "category",
        ]
