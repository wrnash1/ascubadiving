from django.contrib import admin
from django.contrib import admin
from diveshopmanagement.models import (
    GasComposition,
    Tank,
    Airfill,
    GasBlending,
    HydrostaticTest,
    TankInventory,
)

admin.site.register(GasComposition)
admin.site.register(Tank)
admin.site.register(Airfill)
admin.site.register(GasBlending)
admin.site.register(HydrostaticTest)
admin.site.register(TankInventory)
