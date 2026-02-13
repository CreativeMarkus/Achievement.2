import os
import sys
import django

sys.path.insert(0, 'A2_Recipe_App/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print("\n=== Recreating User Accounts ===\n")

# Delete existing users if they exist
User.objects.filter(username__in=['mentorCF', 'Markus']).delete()
print("✅ Deleted existing users")

# Create mentorCF superuser
mentorCF = User.objects.create_superuser(
    username='mentorCF',
    email='mentor@careerfoundry.com',
    password='Ment0r@CareerF0undry'
)
print(f"✅ Created mentorCF superuser")

# Create Markus superuser
markus = User.objects.create_superuser(
    username='Markus',
    email='markus@careerfoundry.com',
    password='Ment0r@CareerF0undry'
)
print(f"✅ Created Markus superuser")

print("\n=== Testing Authentication ===\n")

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

print("\n=== User Setup Complete ===")
print("Users in database:")
for user in User.objects.all().order_by('username'):
    print(f"  - {user.username} (superuser: {user.is_superuser})")
print()
