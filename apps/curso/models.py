from django.db import models

# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    tecnologias = models.CharField(max_length=200)
    creado_en = models.DateTimeField(auto_now_add=True)