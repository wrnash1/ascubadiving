from django.contrib import admin
from .models import EquipmentRepair


class EquipmentRepairAdmin(admin.ModelAdmin):
    list_display = ("name", "date_of_repair", "equipment_repaired")

admin.site.register(EquipmentRepair, EquipmentRepairAdmin)
