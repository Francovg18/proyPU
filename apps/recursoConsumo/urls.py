from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api import (
    DepartamentoViewSet,
    MedidorViewSet,
    ConsumoViewSet,
    AlertaViewSet,
    PagoViewSet,
    MorosidadViewSet
)

router = DefaultRouter()
router.register(r'departamento', DepartamentoViewSet)
router.register(r'medidor', MedidorViewSet)
router.register(r'consumo', ConsumoViewSet)
router.register(r'alerta', AlertaViewSet)
router.register(r'pago', PagoViewSet)
router.register(r'morosidad', MorosidadViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
