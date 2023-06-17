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
list_display == [GasComposition.gas_type, GasComposition.oxygen_percentage]
admin.site.register(Tank)
list_display == [
    Tank.tank_identifier,
    Tank.size,
    Tank.location,
    Tank.hydro_dropoff_date,
    Tank.hydro_pickup_date,
    Tank.hydro_passed,
]
admin.site.register(Airfill)
admin.site.register(GasBlending)
admin.site.register(HydrostaticTest)
admin.site.register(TankInventory)
