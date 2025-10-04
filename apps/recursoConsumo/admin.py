from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Departamento, Medidor, Consumo, Alerta, Pago, Morosidad
from .resources import MorosidadResource, ConsumoResource


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'torre', 'habitantes', 'propietario_id')
    search_fields = ('torre', 'numero')


@admin.register(Medidor)
class MedidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'codigo', 'tipo_servicio_id', 'departamento', 'activo')
    list_filter = ('tipo_servicio_id', 'activo')


@admin.register(Consumo)
class ConsumoAdmin(ImportExportModelAdmin):
    resource_class = ConsumoResource
    list_display = (
        'id',
        'departamento',
        'usuario',
        'fecha',
        'consumo_agua_m3',
        'consumo_luz_kwh',
        'consumo_gas_m3',
        'consumo_total'
    )
    list_filter = ('departamento', 'usuario', 'fecha')


@admin.register(Alerta)
class AlertaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consumo', 'tipo_alerta', 'fecha_alerta', 'estado')


@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ('id', 'monto_pagado', 'fecha_pago', 'metodo_pago')


@admin.register(Morosidad)
class MorosidadAdmin(ImportExportModelAdmin):
    resource_class = MorosidadResource
    list_display = (
        'id',
        'cuenta',
        'emision',
        'convenio',
        'morosidad',
        'anio',
        'departamento',
        'monto_deuda',
        'estado'
    )
