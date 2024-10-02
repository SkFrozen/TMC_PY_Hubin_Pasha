from django.contrib import admin
from django.contrib.auth.models import Group

from .forms import UserAdmin
from .models import Category, FDUser, Food, Order

admin.site.register([Category, Food, Order])
admin.site.register(FDUser, UserAdmin)
admin.site.unregister(Group)
