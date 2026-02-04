from django.test import TestCase
from .models import Recipe

class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name="Test Recipe",
            cooking_time=10,
            description="Test description",
            instructions="Test instructions"
        )

    def test_recipe_name_label(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_recipe_name_max_length(self):
        recipe = Recipe.objects.get(id=1)
        max_length = recipe._meta.get_field('name').max_length
        self.assertEqual(max_length, 120)

    def test_str_method(self):
        recipe = Recipe.objects.get(id=1)
        self.assertEqual(str(recipe), "Test Recipe")
