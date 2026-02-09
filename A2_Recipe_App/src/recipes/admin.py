from django.contrib import admin
from .models import Recipe

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'cooking_time')
    fields = ('name', 'ingredients', 'instructions', 'cooking_time', 'pic')

admin.site.register(Recipe, RecipeAdmin)
