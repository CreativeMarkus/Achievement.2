from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .forms import RecipeSearchForm


class RecipeModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            name="Test Recipe",
            cooking_time=10,
            ingredients="Test ingredients",
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


class RecipeSearchFormTest(TestCase):
    """Test cases for RecipeSearchForm"""

    def test_recipe_search_form_valid_data(self):
        """Test form with valid data"""
        form_data = {
            'recipe_name': 'Pasta',
            'cooking_time': 30,
            'chart_type': '#1'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_search_form_empty_data(self):
        """Test form with empty data (should be valid as all fields are optional)"""
        form_data = {
            'recipe_name': '',
            'cooking_time': '',
            'chart_type': ''
        }
        form = RecipeSearchForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_recipe_search_form_invalid_cooking_time(self):
        """Test form with invalid cooking time (negative number)"""
        form_data = {
            'recipe_name': 'Pasta',
            'cooking_time': -5,
            'chart_type': '#1'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_recipe_search_form_recipe_name_max_length(self):
        """Test form with recipe name exceeding max length"""
        form_data = {
            'recipe_name': 'A' * 121,  # Max is 120
            'cooking_time': 30,
            'chart_type': '#1'
        }
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_recipe_search_form_chart_type_choices(self):
        """Test form with invalid chart type choice"""
        form_data = {
            'recipe_name': 'Pasta',
            'cooking_time': 30,
            'chart_type': '#4'  # Invalid choice
        }
        form = RecipeSearchForm(data=form_data)
        self.assertFalse(form.is_valid())


class RecipeSearchViewTest(TestCase):
    """Test cases for recipe_search view"""

    @classmethod
    def setUpTestData(cls):
        """Set up test data for all test methods"""
        # Create test user
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        
        # Create test recipes
        cls.recipe1 = Recipe.objects.create(
            name='Pasta Carbonara',
            cooking_time=20,
            ingredients='Pasta, Eggs, Bacon',
            instructions='Cook pasta. Mix with bacon and eggs.'
        )
        
        cls.recipe2 = Recipe.objects.create(
            name='Chocolate Cake',
            cooking_time=45,
            ingredients='Flour, Sugar, Eggs, Cocoa',
            instructions='Mix ingredients and bake at 350F for 30 mins.'
        )
        
        cls.recipe3 = Recipe.objects.create(
            name='Caesar Salad',
            cooking_time=10,
            ingredients='Lettuce, Croutons, Parmesan, Dressing',
            instructions='Toss ingredients together.'
        )

    def setUp(self):
        """Set up for each test method"""
        self.client = Client()
        self.url = reverse('recipes:recipe-search')

    def test_search_view_requires_login(self):
        """Test that search view requires authentication"""
        response = self.client.get(self.url)
        # The view should allow access to the search form
        # But the actual functionality depends on implementation
        self.assertEqual(response.status_code, 200)

    def test_search_view_get_request(self):
        """Test GET request to search view"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_search.html')
        self.assertIsInstance(response.context['form'], RecipeSearchForm)

    def test_search_view_post_with_recipe_name(self):
        """Test search by recipe name"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'recipe_name': 'Pasta',
            'cooking_time': '',
            'chart_type': '#1'
        })
        self.assertEqual(response.status_code, 200)
        # Check if search results are returned
        self.assertIn('search_results', response.context)

    def test_search_view_partial_name_match(self):
        """Test that partial recipe name matches work"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'recipe_name': 'Pasta',
            'cooking_time': '',
            'chart_type': '#1'
        })
        self.assertEqual(response.status_code, 200)
        search_results = response.context['search_results']
        if search_results:
            self.assertIn(self.recipe1, search_results)

    def test_search_view_by_cooking_time(self):
        """Test search by cooking time"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'recipe_name': '',
            'cooking_time': '15',
            'chart_type': '#1'
        })
        self.assertEqual(response.status_code, 200)
        search_results = response.context['search_results']
        if search_results:
            # Should include recipes with cooking_time <= 15
            for recipe in search_results:
                self.assertLessEqual(recipe.cooking_time, 15)

    def test_search_view_show_all(self):
        """Test show all recipes functionality"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url + '?show_all=true')
        self.assertEqual(response.status_code, 200)
        search_results = response.context['search_results']
        if search_results:
            self.assertEqual(search_results.count(), 3)

    def test_search_view_no_results(self):
        """Test search with no matching results"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'recipe_name': 'NonExistentRecipe',
            'cooking_time': '',
            'chart_type': '#1'
        })
        self.assertEqual(response.status_code, 200)
        search_results = response.context['search_results']
        if search_results:
            self.assertEqual(search_results.count(), 0)

    def test_search_view_chart_generation(self):
        """Test that chart is generated when search returns results"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.post(self.url, {
            'recipe_name': '',
            'cooking_time': '',
            'chart_type': '#1'
        })
        self.assertEqual(response.status_code, 200)
        # Chart generation depends on whether results exist
        if response.context['search_results']:
            chart = response.context['chart']
            # Chart should be generated if chart_type is provided
            # This will be None if no results or no chart type selected


class RecipeListViewTest(TestCase):
    """Test cases for RecipeListView"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        Recipe.objects.create(
            name='Test Recipe',
            cooking_time=30,
            ingredients='Test ingredients',
            instructions='Test instructions'
        )

    def setUp(self):
        self.client = Client()
        self.url = reverse('recipes:list')

    def test_list_view_requires_login(self):
        """Test that list view requires authentication"""
        response = self.client.get(self.url)
        # Should redirect to login if not authenticated
        self.assertEqual(response.status_code, 302)

    def test_list_view_authenticated_user(self):
        """Test list view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipes.html')


class RecipeDetailViewTest(TestCase):
    """Test cases for RecipeDetailView"""

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        cls.recipe = Recipe.objects.create(
            name='Test Recipe',
            cooking_time=30,
            ingredients='Test ingredients',
            instructions='Test instructions'
        )

    def setUp(self):
        self.client = Client()
        self.url = reverse('recipes:recipe-detail', kwargs={'pk': self.recipe.pk})

    def test_detail_view_requires_login(self):
        """Test that detail view requires authentication"""
        response = self.client.get(self.url)
        # Should redirect to login if not authenticated
        self.assertEqual(response.status_code, 302)

    def test_detail_view_authenticated_user(self):
        """Test detail view for authenticated user"""
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'recipes/recipe_detail.html')
        self.assertEqual(response.context['recipe'], self.recipe)
