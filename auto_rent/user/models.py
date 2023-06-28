from django.db import models


class User(models.Model):
    user = models.TextField()
    number = models.TextField()
    
