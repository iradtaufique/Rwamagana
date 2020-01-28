from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import District, Sector, KPI, Department, Umuryango, Cell, Village


class UmuryangoDisplay(admin.ModelAdmin):
    list_display = ('name', 'number_of_member', 'icyiciro', 'irangamuntu',
                    'kpi', 'sector', 'cell', 'village')
    search_fields = ('name', 'irangamuntu', 'sector__name', 'cell__name', 'village__name')


class CellDisplay(admin.ModelAdmin):
    list_display = ('name', 'sector')
    search_fields = ('name', 'sector__name')


class VillageDisplay(admin.ModelAdmin):
    list_display = ('name', 'cell')
    search_fields = ('name', 'cell__name')

admin.site.site_header = 'Rwamagana District Human Security issues'
admin.site.index_title = 'Admin Dashboard'

admin.site.register(District)
admin.site.register(Sector)
admin.site.register(KPI)
admin.site.register(Department)
admin.site.register(Umuryango, UmuryangoDisplay)
admin.site.register(Village, VillageDisplay)
admin.site.register(Cell, CellDisplay)


