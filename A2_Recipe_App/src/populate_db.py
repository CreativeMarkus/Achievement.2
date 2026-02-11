from recipes.models import Recipe

# Clear existing recipes
Recipe.objects.all().delete()

# Create test recipes
recipes_data = [
    {"name": "Spaghetti Carbonara", "cooking_time": 20, "ingredients": "Pasta, Eggs, Bacon, Cheese", "instructions": "Cook pasta and mix with bacon and eggs."},
    {"name": "Chocolate Cake", "cooking_time": 45, "ingredients": "Flour, Sugar, Eggs, Cocoa", "instructions": "Mix ingredients and bake at 350F."},
    {"name": "Caesar Salad", "cooking_time": 10, "ingredients": "Lettuce, Croutons, Parmesan, Dressing", "instructions": "Toss ingredients together."},
    {"name": "Pad Thai", "cooking_time": 25, "ingredients": "Rice noodles, Shrimp, Peanuts, Lime", "instructions": "Stir-fry ingredients."},
    {"name": "Beef Stew", "cooking_time": 90, "ingredients": "Beef, Potatoes, Carrots, Onions", "instructions": "Simmer for 90 minutes."},
    {"name": "Chicken Pasta", "cooking_time": 35, "ingredients": "Pasta, Chicken, Garlic, Tomato", "instructions": "Cook pasta and chicken, combine with sauce."},
]

for recipe_data in recipes_data:
    Recipe.objects.create(**recipe_data)

print("Test data created successfully!")
