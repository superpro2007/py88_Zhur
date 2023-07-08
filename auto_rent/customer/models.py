from django.db import models


class Customer(models.Model):
    customer = models.TextField()
    number = models.TextField()
    
