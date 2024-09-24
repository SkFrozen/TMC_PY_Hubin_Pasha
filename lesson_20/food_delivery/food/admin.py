from django.contrib import admin

from .models import Category, FDUser, Food, Order

admin.site.register([Category, FDUser, Food, Order])
