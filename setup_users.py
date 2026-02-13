import os
import sys
import django

sys.path.insert(0, 'A2_Recipe_App/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User

print("\n=== Setting Up User Accounts ===\n")

# Setup mentorCF superuser
if User.objects.filter(username='mentorCF').exists():
    user = User.objects.get(username='mentorCF')
    user.set_password('Ment0r@CareerF0undry')
    user.save()
    print("✅ Updated mentorCF password")
else:
    User.objects.create_superuser('mentorCF', 'mentor@careerfoundry.com', 'Ment0r@CareerF0undry')
    print("✅ Created mentorCF superuser")

# Setup Markus superuser/staff user
if User.objects.filter(username='Markus').exists():
    user = User.objects.get(username='Markus')
    user.set_password('Ment0r@CareerF0undry')
    user.save()
    print("✅ Updated Markus password")
else:
    User.objects.create_superuser('Markus', 'markus@careerfoundry.com', 'Ment0r@CareerF0undry')
    print("✅ Created Markus superuser")

print("\n=== User Setup Complete ===\n")
print("Login credentials:")
print("  Username: mentorCF or Markus")
print("  Password: Ment0r@CareerF0undry")
print()
