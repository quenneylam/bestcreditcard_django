from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50, default="")
    price = models.CharField(max_length=50, default="")
    description = models.CharField(max_length=250, default="")
    image = models.ImageField(max_length=50, default="")

    def __str__(self):
        return str(self.name)

