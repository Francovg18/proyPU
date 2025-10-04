from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import Consumo, Morosidad, Departamento
from django.contrib.auth.models import User

# --- Morosidad ---
class MorosidadResource(resources.ModelResource):
    class Meta:
        model = Morosidad
        fields = (
            'id',
            'cuenta',
            'emision',
            'convenio',
            'morosidad',
            'anio',
            'monto_deuda',
            'estado'
        )

# --- Consumo ---
class ConsumoResource(resources.ModelResource):
    departamento = fields.Field(
        column_name='departamento',
        attribute='departamento',
        widget=ForeignKeyWidget(Departamento, 'id')
    )
    usuario = fields.Field(
        column_name='usuario',
        attribute='usuario',
        widget=ForeignKeyWidget(User, 'id')
    )

    class Meta:
        model = Consumo
        fields = (
            'id',
            'departamento',
            'usuario',
            'fecha',
            'consumo_agua_m3',
            'consumo_luz_kwh',
            'consumo_gas_m3',
            'consumo_total'
        )

    def before_import_row(self, row, **kwargs):
        """Antes de importar cada fila, valida que usuario y departamento existan."""
        # Departamento
        dep_id = row.get('departamento')
        if dep_id:
            try:
                Departamento.objects.get(id=dep_id)
            except Departamento.DoesNotExist:
                row['departamento'] = None
        else:
            row['departamento'] = None

        # Usuario
        user_id = row.get('usuario')
        if user_id:
            try:
                User.objects.get(id=user_id)
            except User.DoesNotExist:
                row['usuario'] = None
        else:
            row['usuario'] = None
