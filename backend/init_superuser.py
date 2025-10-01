import os
import django
import time
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flight_manager.settings")
django.setup()

User = get_user_model()

# Esperar hasta que la DB esté lista
max_retries = 30
for i in range(max_retries):
    try:
        if User.objects.exists():
            break
        else:
            User.objects.create_superuser(
                username=os.getenv("DJANGO_SUPERUSER_USERNAME", "admin"),
                email=os.getenv("DJANGO_SUPERUSER_EMAIL", "admin@example.com"),
                password=os.getenv("DJANGO_SUPERUSER_PASSWORD", "adminpass"),
            )
            print("Superusuario creado")
            break
    except Exception:
        print("⏳ Esperando a que la DB y auth estén listas...")
        time.sleep(2)
