import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipe_project.settings')
import django
django.setup()

from recipes.models import Recipe
from pathlib import Path
from django.conf import settings

print("=== DATABASE ENTRIES ===")
for r in Recipe.objects.all():
    print(f"  {r.name} | pic.name={r.pic.name} | pic.url={r.pic.url}")

print("\n=== MEDIA_ROOT ===")
print(f"  {settings.MEDIA_ROOT}")

print("\n=== FILES IN MEDIA_ROOT ===")
media_path = Path(settings.MEDIA_ROOT)
if media_path.exists():
    for f in media_path.iterdir():
        print(f"  {f.name}")
else:
    print("  MEDIA_ROOT DOES NOT EXIST!")
