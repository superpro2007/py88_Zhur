from django.db import models
from auto.models import Car
from customer.models import Customer


class Rent(models.Model):
    car  =  models.ForeignKey(Car, null=False, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, null=False, on_delete=models.CASCADE)
    