import os
import sys
import django

# Add the src directory to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'A2_Recipe_App', 'src'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User

users = User.objects.all()
print(f"\nTotal users in database: {users.count()}\n")
for user in users:
    print(f"Username: {user.username}")
    print(f"  Email: {user.email}")
    print(f"  Superuser: {user.is_superuser}")
    print(f"  Staff: {user.is_staff}")
    print()
