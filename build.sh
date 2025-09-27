set -o errexit

pip install -r requirements.txt

python manage.py collectstatic
python manage.py migrate
python manage.py makemigrations



echo "Creando superusuario automáticamente..."

python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

# Solo lo creamos si no existe un superusuario con ese email
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
