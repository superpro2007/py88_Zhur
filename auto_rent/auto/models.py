from django.db import models


class Car(models.Model):
    brand = models.TextField()
    model = models.TextField()
    vin = models.TextField(unique=True)
