from django.db import models
from django.contrib.auth.models import User

# Departamento
class Departamento(models.Model):
    numero = models.IntegerField()
    torre = models.CharField(max_length=50)
    propietario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Torre {self.torre} - Dep {self.numero}"


# Medidor
class Medidor(models.Model):
    TIPO_SERVICIO_CHOICES = [
        (1, 'Agua'),
        (2, 'Luz'),
        (3, 'Gas')
    ]
    tipo_servicio_id = models.IntegerField(choices=TIPO_SERVICIO_CHOICES)
    codigo = models.CharField(max_length=15)
    activo = models.BooleanField(default=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='medidores')

    def __str__(self):
        return f"{self.codigo} - {self.get_tipo_servicio_id_display()}"


# Consumo
class Consumo(models.Model):
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE, related_name='consumos')
    tipo_servicio_id = models.IntegerField(choices=Medidor.TIPO_SERVICIO_CHOICES)
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    fecha = models.DateField()
    periodo = models.DateField()
    consumo_agua_m3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    consumo_luz_kwh = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    consumo_gas_m3 = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    consumo_total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Alerta
class Alerta(models.Model):
    consumo = models.ForeignKey(Consumo, on_delete=models.CASCADE, related_name='alertas')
    tipo_alerta = models.CharField(max_length=50)
    descripcion = models.TextField()
    fecha_alerta = models.DateTimeField(auto_now_add=True)  # fecha por defecto ahora
    estado = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


# Pago
class Pago(models.Model):
    factura_id = models.IntegerField()
    monto_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_pago = models.DateTimeField(auto_now_add=True)
    codigo_qr = models.TextField(null=True, blank=True)
    referencia_transaccion = models.TextField(null=True, blank=True)
    metodo_pago = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)


# Morosidad
class Morosidad(models.Model):
    factura_id = models.IntegerField()
    cuenta = models.CharField(max_length=50)
    emision = models.DecimalField(max_digits=10, decimal_places=2)
    convenio = models.DecimalField(max_digits=10, decimal_places=2)
    morosidad = models.DecimalField(max_digits=10, decimal_places=2)
    anio = models.IntegerField()
    monto_deuda = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)
