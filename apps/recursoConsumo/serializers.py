from rest_framework import serializers
from .models import Departamento, Medidor, Consumo, Alerta, Pago, Morosidad

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class MedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = '__all__'

class ConsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consumo
        fields = '__all__'

class AlertaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerta
        fields = '__all__'

class PagoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pago
        fields = '__all__'

class MorosidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Morosidad
        fields = '__all__'
