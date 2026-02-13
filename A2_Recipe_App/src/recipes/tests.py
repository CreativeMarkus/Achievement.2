from django.test import TestCase
from django.urls import reverse
from .models import Recipe


class RecipeModelTest(TestCase):

    def setUp(self):
        self.recipe = Recipe.objects.create(
            name="Test Recipe",
            ingredients="Test ingredients",
            cooking_time=10
        )

    def test_recipe_string(self):
        self.assertEqual(str(self.recipe), "Test Recipe")


class RecipeViewTest(TestCase):

    def setUp(self):
        from django.contrib.auth.models import User
        self.user = User.objects.create_user(username='testuser', password='testpass123')

    def test_home_page_status_code(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_list_status_code(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('recipes:list'))
        self.assertEqual(response.status_code, 200)
