from django.db import models
from django.contrib.auth.models import User


class Address(models.Model):
    country = models.CharField(
        max_length=15,
        blank=True
    )
    city = models.CharField(
        max_length=15,
        blank=True
    )
    zip_code = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        blank=True
    )
    address1 = models.CharField(
        max_length=20,
        blank=True
    )
    address2 = models.CharField(
        max_length=20,
        blank=True
    )

    def __str__(self):
        result = f"{self.country}, {self.city}, {self.zip_code}, {self.address1}"
        if self.address2:
            result += f", {self.address2}"
        return result


class Account(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete=models.CASCADE
        )
    phone = models.CharField(
        max_length=15,
        blank=True
    )
    view_personal_info = models.BooleanField(
        default=False
    )
    gender = models.CharField(
        max_length=10,
        gender=[
            ('Мужской','male'),
            ('Женский','female'), 
            ('Не выбран','sex')
            ],
        default="Не выбран"
    )
    address = models.ForeignKey(
        Address, 
        on_delete=models.CASCADE, 
        blank=True, 
        null=True
        )

    def __str__(self):
        return self.user.username