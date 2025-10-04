# recursoConsumo/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    DepartamentoViewSet, MedidorViewSet, ConsumoViewSet,
    AlertaViewSet, PagoViewSet, MorosidadViewSet
)
from . import views 

router = DefaultRouter()
router.register(r'departamento', DepartamentoViewSet)
router.register(r'medidor', MedidorViewSet)
router.register(r'consumo', ConsumoViewSet)
router.register(r'alerta', AlertaViewSet)
router.register(r'pago', PagoViewSet)
router.register(r'morosidad', MorosidadViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Dashboards
    path('api/dashboard/consumo-servicio/', views.consumo_por_servicio),
    path('api/dashboard/morosidad-estado/', views.morosidad_por_estado),
    path('api/dashboard/top-departamentos/', views.top_departamentos_consumo),
    path('api/dashboard/pagos-tiempo/', views.pagos_tiempo),
    path('api/dashboard/alertas-riesgo/', views.alertas_por_riesgo),
    path('api/dashboard/departamentos-info/', views.departamentos_info),
]
