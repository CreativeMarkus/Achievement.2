from django.db import models
from recipes.models import Recipe

class Review(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return str(self.rating)
