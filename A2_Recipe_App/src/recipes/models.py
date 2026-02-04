from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=120)
    cooking_time = models.IntegerField(help_text="in minutes")
    description = models.TextField()
    instructions = models.TextField()

    def __str__(self):
        return str(self.name)
