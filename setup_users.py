import os
import sys
import django

sys.path.insert(0, 'A2_Recipe_App/src')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
django.setup()

from django.contrib.auth.models import User

# Update Markus password
user = User.objects.get(username='Markus')
user.set_password('Ment0r@CareerF0undry')
user.save()
print(f"✅ Updated password for user: {user.username}")

# Create mentorCF as superuser if it doesn't exist
if not User.objects.filter(username='mentorCF').exists():
    User.objects.create_superuser('mentorCF', 'mentor@careerfoundry.com', 'Ment0r@CareerF0undry')
    print("✅ Created mentorCF superuser")
else:
    print("✅ mentorCF user already exists")
