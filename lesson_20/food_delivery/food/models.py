from django.contrib.auth.models import User
from django.db import models


class FDUser(User):
    role = models.CharField(max_length=30)


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name


class Food(models.Model):
    name = models.CharField(max_length=255)
    cost = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders")
    courier = models.ForeignKey(
        FDUser, on_delete=models.CASCADE, related_name="to_order"
    )
    meals = models.ManyToManyField(Food)
    address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.id}-{self.address}"
