set -o errexit

# Instala paquetes
pip install -r requirements.txt

# Copia los static files sin preguntar
python manage.py collectstatic --noinput

# Migraciones
python manage.py migrate
python manage.py makemigrations

# Crear superusuario automáticamente
echo "Creando superusuario automáticamente..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

if not User.objects.filter(email='franco@gmail.com').exists():
    user = User.objects.create_superuser(
        username='Alexito',
        email='franco@gmail.com',
        password='123456'
    )
    print("✅ Superusuario creado con éxito.")
else:
    print("ℹ️ El superusuario ya existe, no se crea de nuevo.")
EOF
