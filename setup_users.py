import os
import sys
import django

sys.path.insert(0, 'A2_Recipe_App/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User

print("\n=== Setting Up User Accounts ===\n")

# Delete and recreate mentorCF superuser
if User.objects.filter(username='mentorCF').exists():
    User.objects.filter(username='mentorCF').delete()
    print("✅ Deleted existing mentorCF")

User.objects.create_superuser('mentorCF', 'mentor@careerfoundry.com', 'Ment0r@CareerF0undry')
print("✅ Created mentorCF superuser")

# Delete and recreate Markus superuser
if User.objects.filter(username='Markus').exists():
    User.objects.filter(username='Markus').delete()
    print("✅ Deleted existing Markus")

User.objects.create_superuser('Markus', 'markus@careerfoundry.com', 'Ment0r@CareerF0undry')
print("✅ Created Markus superuser")

print("\n=== User Setup Complete ===\n")
print("Login credentials:")
print("  Username: mentorCF or Markus")
print("  Password: Ment0r@CareerF0undry")
print()
