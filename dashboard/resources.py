import import_export
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget

from .models import Umuryango, Sector, Cell, Village, KPI


class UmuryangoResource(resources.ModelResource):
    kpi = fields.Field(column_name='kpi', attribute='kpi', widget=ForeignKeyWidget(KPI, 'name'))
    sector = fields.Field(column_name='sector', attribute='sector', widget=ForeignKeyWidget(Sector, 'name'))
    cell = fields.Field(column_name='cell', attribute='cell', widget=ForeignKeyWidget(Cell, 'name'))
    village = fields.Field(column_name='village', attribute='village', widget=ForeignKeyWidget(Village, 'name'))

    class Meta:
        model = Umuryango

