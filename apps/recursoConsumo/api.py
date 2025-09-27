# apps/finanzas/api.py
from rest_framework import viewsets, permissions
from .models import Departamento, Medidor, Consumo, Alerta, Pago, Morosidad
from .serializers import (
    DepartamentoSerializer,
    MedidorSerializer,
    ConsumoSerializer,
    AlertaSerializer,
    PagoSerializer,
    MorosidadSerializer
)

# -------------------------------
# ViewSets para DRF
# -------------------------------

class DepartamentoViewSet(viewsets.ModelViewSet):
    queryset = Departamento.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = DepartamentoSerializer

class MedidorViewSet(viewsets.ModelViewSet):
    queryset = Medidor.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MedidorSerializer

class ConsumoViewSet(viewsets.ModelViewSet):
    queryset = Consumo.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ConsumoSerializer

class AlertaViewSet(viewsets.ModelViewSet):
    queryset = Alerta.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = AlertaSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = PagoSerializer

class MorosidadViewSet(viewsets.ModelViewSet):
    queryset = Morosidad.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = MorosidadSerializer
