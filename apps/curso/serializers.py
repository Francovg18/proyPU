from rest_framework import serializers
from .models import Curso

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ('id', 'titulo', 'descripcion', 'tecnologias', 'creado_en')
        read_only_fields = ('creado_en', )