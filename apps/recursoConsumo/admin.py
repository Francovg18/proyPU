from django.contrib import admin
from .models import Departamento, Medidor, Consumo, Alerta, Pago, Morosidad

@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'torre', 'propietario_id')
    search_fields = ('torre', 'numero')

@admin.register(Medidor)
class MedidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'tipo_servicio_id', 'departamento', 'activo')
    list_filter = ('tipo_servicio_id', 'activo')

@admin.register(Consumo)
class ConsumoAdmin(admin.ModelAdmin):
    list_display = ('id', 'departamento', 'tipo_servicio_id', 'fecha', 'consumo_total')
    list_filter = ('tipo_servicio_id',)

@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumo', 'tipo_alerta', 'fecha_alerta', 'estado')

@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'factura_id', 'monto_pagado', 'fecha_pago', 'metodo_pago')

@admin.register(Morosidad)
class MorosidadAdmin(admin.ModelAdmin):
    list_display = ('id', 'factura_id', 'cuenta', 'monto_deuda', 'estado', 'anio')
