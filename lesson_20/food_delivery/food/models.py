from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


class FDUserManager(BaseUserManager):
    def create_user(self, username, role, password=None):
        if not role:
            raise ValueError("Users must have a role")

        user = self.model(username=username, role=role)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, role, password=None):
        user = self.create_user(username, role, password=password)
        user.is_staff = True
        user.save(using=self._db)
        return user


class FDUser(AbstractBaseUser):
    username = models.CharField(
        verbose_name="username",
        max_length=255,
        unique=True,
    )
    role = models.CharField(max_length=30)
    is_staff = models.BooleanField(default=False)

    objects = FDUserManager()

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["role"]


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
    customer = models.ForeignKey(
        FDUser, on_delete=models.CASCADE, related_name="orders"
    )
    courier = models.ForeignKey(
        FDUser, on_delete=models.CASCADE, related_name="to_order"
    )
    meals = models.ManyToManyField(Food)
    address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"{self.id}-{self.address}"
