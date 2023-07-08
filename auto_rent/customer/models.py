from django.db import models


class Customer(models.Model):
    name = models.TextField()
    number = models.TextField(unique=True)
    
