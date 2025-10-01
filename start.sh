#!/usr/bin/env bash
set -euo pipefail

echo "======================================"
echo "🚀 Inicializando Flight Manager App 🚀"
echo "======================================"

# 1️⃣ Levantar DB y Redis primero
echo "🔹 Levantando DB y Redis..."
docker-compose up -d db redis

# 2️⃣ Levantar backend (el entrypoint.sh hará migraciones, superusuario y Celery)
echo "🔹 Levantando backend..."
docker-compose up -d --build backend

# 3️⃣ Esperar a que el backend esté listo
BACKEND_URL="http://localhost:8000"

echo "🔹 Esperando que el backend responda en $BACKEND_URL..."
until curl -s "$BACKEND_URL" >/dev/null 2>&1; do
    echo "Esperando backend..."
    sleep 2
done
echo "✅ Backend listo"

# 4️⃣ Levantar frontend
echo "🔹 Levantando frontend..."
docker-compose up -d --build frontend

echo "======================================"
echo "✅ Flight Manager App lista para usar ✅"
echo "Frontend: http://localhost:3000"
echo "Backend API: http://localhost:8000/api/"
echo "Admin Django: http://localhost:8000/admin/"
echo "Usuario admin: admin / adminpass"
echo "======================================"
