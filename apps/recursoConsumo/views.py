from django.db.models.functions import TruncMonth
from django.db.models import Sum, Count, F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Departamento, Consumo, Morosidad, Pago, Medidor, Alerta
@api_view(['GET'])
def consumo_por_servicio(request):
    data = Consumo.objects.aggregate(
        total_agua=Sum('consumo_agua_m3'),
        total_luz=Sum('consumo_luz_kwh'),
        total_gas=Sum('consumo_gas_m3'),
    )
    return Response(data)

@api_view(['GET'])
def morosidad_por_estado(request):
    data = Morosidad.objects.values('estado').annotate(total=Count('id'))
    return Response(data)

@api_view(['GET'])
def top_departamentos_consumo(request):
    data = (
        Consumo.objects.values('departamento__torre', 'departamento__numero')
        .annotate(total_consumo=Sum('consumo_total'))
        .order_by('-total_consumo')[:5]
    )
    return Response(data)

@api_view(['GET'])
def pagos_tiempo(request):
    data = (
        Pago.objects.annotate(mes=TruncMonth('fecha_pago'))
        .values('mes')
        .annotate(total=Sum('monto_pagado'))
        .order_by('mes')
    )
    result = [{'mes': d['mes'].strftime('%Y-%m'), 'total': float(d['total'])} for d in data]
    return Response(result)

@api_view(['GET'])
def alertas_por_riesgo(request):
    data = Alerta.objects.values('nivel_riesgo').annotate(total=Count('id'))
    return Response(data)


@api_view(['GET'])
def departamentos_info(request):
    departamentos = Departamento.objects.all()
    result = []

    for dep in departamentos:
        medidores = dep.medidores.all()
        consumos = dep.consumos.all()
        morosidades = dep.morosidades.all()  
        pagos = Pago.objects.filter(morosidad__in=morosidades)
        alertas = Alerta.objects.filter(morosidad__in=morosidades)

        # contar medidores por tipo
        medidores_count = {
            'agua': medidores.filter(tipo_servicio_id=1).count(),
            'luz': medidores.filter(tipo_servicio_id=2).count(),
            'gas': medidores.filter(tipo_servicio_id=3).count(),
        }

        # consumos totales
        total_consumo = consumos.aggregate(
            total_agua=Sum('consumo_agua_m3'),
            total_luz=Sum('consumo_luz_kwh'),
            total_gas=Sum('consumo_gas_m3'),
        )

        # Morosidad y pagos
        total_morosidad = morosidades.aggregate(deuda_total=Sum('monto_deuda'))
        total_pagos = pagos.aggregate(pagos_total=Sum('monto_pagado'))

        # alertas
        alertas_count = alertas.values('nivel_riesgo').annotate(total=Count('id'))
        result.append({
            'id': dep.id,
            'torre': dep.torre,
            'numero': dep.numero,
            'habitantes': dep.habitantes,
            'propietario': dep.propietario.username if dep.propietario else None,
            'medidores': medidores_count,
            'consumo': {k: float(v or 0) for k, v in total_consumo.items()},
            'morosidad_total': float(total_morosidad['deuda_total'] or 0),
            'pagos_total': float(total_pagos['pagos_total'] or 0),
            'alertas': list(alertas_count)
        })

    return Response(result)
