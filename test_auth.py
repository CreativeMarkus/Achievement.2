import os
import sys
import django

sys.path.insert(0, 'A2_Recipe_App/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print("\n=== Testing Authentication ===\n")

# List all users
print("Users in database:")
for user in User.objects.all():
    print(f"  - {user.username} (email: {user.email})")

print("\n" + "="*50)
print("Testing credentials:")
print("="*50 + "\n")

# Test mentorCF
result = authenticate(username='mentorCF', password='Ment0r@CareerF0undry')
if result:
    print("✅ mentorCF authentication: SUCCESS")
else:
    print("❌ mentorCF authentication: FAILED")

# Test Markus
result = authenticate(username='Markus', password='Ment0r@CareerF0undry')
if result:
    print("✅ Markus authentication: SUCCESS")
else:
    print("❌ Markus authentication: FAILED")

print()
