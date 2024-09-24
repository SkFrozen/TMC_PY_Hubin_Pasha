from django.shortcuts import render

from .models import Category


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}

    return render(request, "food/category.html", context)


def edit_category(request, id):
    category = Category.objects.get(id=id)
