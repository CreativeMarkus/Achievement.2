#!/usr/bin/env python
"""
Diagnostic script to check authentication issues on production.
This helps identify if users exist and if authentication works.
"""
import os
import sys
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

print("\n" + "="*60)
print("AUTHENTICATION DIAGNOSTIC REPORT")
print("="*60)

# Check if users exist
print("\n1. CHECKING USERS IN DATABASE:")
users = User.objects.all()
print(f"   Total users: {users.count()}")

if users.count() == 0:
    print("   ⚠️  NO USERS FOUND IN DATABASE!")
    print("   → You need to run: heroku run 'python setup_users.py' -a my-recipe-app")
else:
    for user in users:
        print(f"\n   Username: {user.username}")
        print(f"   Email: {user.email}")
        print(f"   Is Superuser: {user.is_superuser}")
        print(f"   Is Staff: {user.is_staff}")
        print(f"   Password hash exists: {bool(user.password)}")

# Test authentication  
print("\n2. TESTING AUTHENTICATION:")
test_credentials = [
    ("mentorCF", "Ment0r@CareerF0undry"),
    ("Markus", "Ment0r@CareerF0undry"),
]

for username, password in test_credentials:
    user = authenticate(username=username, password=password)
    if user is not None:
        print(f"   ✅ {username}: Authentication SUCCESSFUL")
    else:
        print(f"   ❌ {username}: Authentication FAILED")
        # Check if user exists
        try:
            db_user = User.objects.get(username=username)
            print(f"      → User exists in DB, but password doesn't match")
        except User.DoesNotExist:
            print(f"      → User does NOT exist in database")

print("\n" + "="*60)
print("If issues are found, run: heroku run 'python setup_users.py' -a my-recipe-app")
print("="*60 + "\n")
