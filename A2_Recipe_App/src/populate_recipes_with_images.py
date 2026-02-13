import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from recipes.models import Recipe
from django.core.files.base import ContentFile
from pathlib import Path

# Clear existing recipes
Recipe.objects.all().delete()

# Get the recipes static folder
recipes_folder = Path(__file__).parent / 'recipes' / 'static' / 'recipes' / 'images'

# Image file to recipe mapping
recipes_data = [
    {"name": "Spaghetti Carbonara", "cooking_time": 20, "ingredients": "Pasta, Eggs, Bacon, Cheese", "instructions": "Cook pasta and mix with bacon and eggs.", "image": "aglio-e-olio-recipe-2023-7.jpg"},
    {"name": "Chocolate Brownies", "cooking_time": 45, "ingredients": "Flour, Sugar, Eggs, Cocoa, Butter", "instructions": "Mix ingredients and bake at 350F.", "image": "brownies.jpg"},
    {"name": "Chicken Noodle Soup", "cooking_time": 30, "ingredients": "Chicken, Noodles, Broth, Vegetables", "instructions": "Simmer all ingredients together.", "image": "chicken-noodle-soup-2026-01-05-06-08-25-utc.jpg"},
    {"name": "Creamy Garlic Butter Shrimp", "cooking_time": 15, "ingredients": "Shrimp, Garlic, Butter, Cream", "instructions": "Sauté shrimp in garlic butter cream sauce.", "image": "Creamy_Garlic_Butter_Shrimp.png"},
    {"name": "Homemade Pizza with Salami", "cooking_time": 35, "ingredients": "Dough, Tomato Sauce, Cheese, Salami", "instructions": "Prepare dough, add toppings, bake at 450F.", "image": "homemade-pizza-with-salami-2026-01-09-08-19-34-utc.jpg"},
    {"name": "One-Pot Thai Red Curry", "cooking_time": 25, "ingredients": "Coconut Milk, Thai Red Curry Paste, Vegetables, Chicken", "instructions": "Combine ingredients and simmer.", "image": "One-Pot-Thai-Red-Curry.png"},
    {"name": "Pan-Seared Ribeye with Rosemary", "cooking_time": 20, "ingredients": "Ribeye Steak, Rosemary, Butter, Garlic", "instructions": "Pan sear steak with herbs.", "image": "Pan-Seare-Ribeye-with-Rosemary.jpg"},
    {"name": "Roasted Sweet Potato Chickpea Buddha Bowl", "cooking_time": 40, "ingredients": "Sweet Potatoes, Chickpeas, Vegetables, Dressing", "instructions": "Roast vegetables and chickpeas, serve in bowl.", "image": "Roasted_Sweet_Potato__Chickpea_Buddha_Bowl.png"},
    {"name": "Shakshuka", "cooking_time": 25, "ingredients": "Eggs, Tomatoes, Onions, Spices", "instructions": "Poach eggs in tomato sauce.", "image": "Shakshuka.png"},
]

for recipe_data in recipes_data:
    image_filename = recipe_data.pop("image")
    image_path = recipes_folder / image_filename
    
    # Create recipe without image first
    recipe = Recipe.objects.create(**recipe_data)
    
    # If image exists, add it to the recipe
    if image_path.exists():
        with open(image_path, 'rb') as img_file:
            recipe.pic.save(image_filename, ContentFile(img_file.read()), save=True)
        print(f"Created recipe: {recipe.name} with image: {image_filename}")
    else:
        print(f"Created recipe: {recipe.name} (image not found)")

print("Recipe data created successfully!")
