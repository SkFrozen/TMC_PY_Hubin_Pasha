from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic import DetailView, ListView

from .forms import CategoryForm, CreateUserForm, EditUserForm, FoodForm
from .models import Category, FDUser, Food, Order

"""Category Views"""


def category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "food/category.html", context)


def edit_category(request, id):
    if request.method == "GET":
        category = Category.objects.get(id=id)
        cat_form = CategoryForm(instance=category)
        context = {"cat_form": cat_form, "id": category.id}
        return render(request, "edit_category.html", context)
    elif request.method == "POST":
        edited_cat = Category.objects.get(id=id)
        edited_cat.name = request.POST.get("name")
        edited_cat.save()
        return redirect("/food/category")


def delete_category(request, id):
    category = Category.objects.get(id=id)
    category.delete()
    return redirect("/food/category")


class CreateCategory(DetailView):

    def get(self, request):
        cat_form = CategoryForm(request.POST)
        context = {"cat_form": cat_form}
        return render(request, "create_category.html", context)

    def post(self, request):
        cat_form = CategoryForm(request.POST)
        cat_form.save()
        return redirect("/food/category")


"""FDUser Views"""


class FDUserListView(ListView):
    model = FDUser


class EditFDUser(DetailView):
    model = FDUser
    template_name = "edit_fduser.html"

    def get(self, request, id):
        user = self.model.objects.get(id=id)
        user_form = EditUserForm(instance=user)
        context = {"id": user.id, "user_form": user_form}
        return render(request, self.template_name, context)

    def post(self, request, id):
        user = self.model.objects.get(id=id)
        user_form = EditUserForm(request.POST, instance=user)
        if user_form.is_valid():
            user_form.save()
            return redirect("/food/users")
        context = {"user_form": user_form}
        return render(request, self.template_name, context)


class CreateFDUser(DetailView):
    model = FDUser
    template_name = "create_fduser.html"

    def get(self, request):
        user_form = CreateUserForm()
        context = {"user_form": user_form}
        return render(request, self.template_name, context)

    def post(self, request):
        user_form = CreateUserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("/food/users")
        context = {"user_form": user_form}
        return render(request, self.template_name, context)


def delete_user(request, id):
    user = FDUser.objects.get(id=id)
    user.delete()
    return redirect("/food/users")


"""Food Views"""


class FoodListView(ListView):
    model = Food


class EditFood(DetailView):
    model = Food
    template_name = "edit_food.html"

    def get(self, request, id):
        food = self.model.objects.get(id=id)
        food_form = FoodForm(instance=food)
        context = {"id": food.id, "food_form": food_form}
        return render(request, self.template_name, context)

    def post(self, request, id):
        food = self.model.objects.get(id=id)
        food_form = FoodForm(request.POST, instance=food)
        if food_form.is_valid():
            food_form.save()
            return redirect("/food")
        context = {"food_form": food_form}
        return render(request, self.template_name, context)


class CreateFood(DetailView):
    model = Food
    template_name = "create_food.html"

    def get(self, request):
        food_form = FoodForm()
        context = {"food_form": food_form}
        return render(request, self.template_name, context)

    def post(self, request):
        food_form = FoodForm(request.POST)
        if food_form.is_valid():
            food_form.save()
            return redirect("/food")
        context = {"food_form": food_form}
        return render(request, self.template_name, context)


def delete_food(request, id):
    food = Food.objects.get(id=id)
    food.delete()
    return redirect("/food")
