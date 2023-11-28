from django.db import models


class Diet(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    ingredients = models.TextField()  # Field to store the list of ingredients
    instructions = models.TextField()  # Field to store cooking instructions or steps
