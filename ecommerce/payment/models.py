from django.contrib.auth.models import User
from django.db import models
from ecommerce.core.models import Product


class Payment(models.Model):
    user = models.ForeignKey('auth.User', on_delete=True)
    product = models.ForeignKey(Product, on_delete=True)
    address = models.CharField(max_length=250)
    state = models.CharField(max_length=90)
    city = models.CharField(max_length=120)
    card_name = models.CharField(max_length=200, null=True)
    card_number = models.CharField(max_length=18, null=True)
    expiring_month = models.DateField(null=True)
    expiring_year = models.DateField(null=True)
    card_cvv = models.CharField(max_length=3, null=True)