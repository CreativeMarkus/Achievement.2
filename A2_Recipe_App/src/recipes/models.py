from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    ingredients = models.TextField(blank=True, null=True)
    instructions = models.TextField(blank=True, null=True)
    cooking_time = models.IntegerField()
    pic = models.ImageField(upload_to='recipes', default='no_picture.jpg')

    def __str__(self):
        return self.name
