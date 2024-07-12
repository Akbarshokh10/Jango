from django.db import models

# Create your models here.

class Card(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    image = models.ImageField(null=True, blank=True, upload_to="images/")


class About(models.Model):
    name = models.CharField(max_length=250)
    about = models.CharField(max_length=500)
    how_much = models.CharField(max_length=250)