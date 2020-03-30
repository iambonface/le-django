from django.db import models

# Create your models here.
class Product(models.Model):
    title        = models.TextField()
    description  = models.TextField()
    price        = models.DecimalField(max_digits=11, decimal_places=2)
    availability = models.BooleanField(default=False)

