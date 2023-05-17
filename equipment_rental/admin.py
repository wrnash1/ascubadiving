from django.contrib import admin
from .models import Equipment, Rental, RentalEquipment


class RentalEquipmentInline(admin.TabularInline):
    model = RentalEquipment


class RentalAdmin(admin.ModelAdmin):
    inlines = [
        RentalEquipmentInline,
    ]
    list_display = ("id", "diver", "date_of_rental", "date_due")


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ("name", "serial_number", "condition")


admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Rental, RentalAdmin)
