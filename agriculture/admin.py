from django.contrib import admin

from agriculture.models import (Crops, Seeds, Banana_and_Rehabilitation, Ubwanikiro, Vaccination,
                                Umuhigo, UnusedTerassis, InkaZizakurikiranwa, Insemination, Pumps_in_Sector,
                                Ha_irrigated, Fertilizers, Girinka, Trainings)


class Inka_admin(admin.ModelAdmin):
    list_display = ('inka_zizakurikiranwa', 'sector', 'achieved')


admin.site.register(Crops)
admin.site.register(Seeds)
admin.site.register(Banana_and_Rehabilitation)
admin.site.register(Ubwanikiro)
admin.site.register(Vaccination)
admin.site.register(Umuhigo)
admin.site.register(UnusedTerassis)
admin.site.register(Insemination)
admin.site.register(InkaZizakurikiranwa, Inka_admin)
admin.site.register(Pumps_in_Sector)
admin.site.register(Ha_irrigated)
admin.site.register(Fertilizers)
admin.site.register(Girinka)
admin.site.register(Trainings)