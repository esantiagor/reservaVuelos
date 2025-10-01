#!/usr/bin/env bash
set -euo pipefail

echo "🔹 Esperando a que la base de datos esté lista..."

# Espera a que Postgres responda
until python - <<EOF
import sys
import psycopg2
import os

db_name = os.getenv("POSTGRES_DB")
db_user = os.getenv("POSTGRES_USER")
db_pass = os.getenv("POSTGRES_PASSWORD")
db_host = os.getenv("POSTGRES_HOST", "db")
db_port = os.getenv("POSTGRES_PORT", "5432")

try:
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_pass,
        host=db_host,
        port=db_port,
    )
    conn.close()
except Exception:
    sys.exit(1)
EOF
do
    echo "⏳ Esperando DB..."
    sleep 2
done

echo "✅ Base de datos lista"

echo "🔹 Aplicando migraciones..."
python manage.py migrate

echo "🔹 Creando superusuario si no existe..."
python init_superuser.py

echo "🔹 Cargando datos iniciales..."
python manage.py shell < init_destinations.py

echo "✅ Django listo, iniciando servidor y Celery..."

# Inicia Celery en background
celery -A flight_manager worker --loglevel=info &

# Ejecuta el servidor de Django
exec python manage.py runserver 0.0.0.0:8000
