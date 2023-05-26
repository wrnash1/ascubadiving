from django.contrib import admin
from diveshopmanagement.models import (
    Customer,
    Organization,
    Certification,
    Equipment,
    EquipmentInventory,
    DiveSite,
    DiveLog,
)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    pass


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(EquipmentInventory)
class EquipmentInventoryAdmin(admin.ModelAdmin):
    pass


@admin.register(DiveSite)
class DiveSiteAdmin(admin.ModelAdmin):
    pass


@admin.register(DiveLog)
class DiveLogAdmin(admin.ModelAdmin):
    pass
