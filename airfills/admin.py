from django.contrib import admin
from diveshopmanagement.models import Airfill



@admin.register(Airfill)
class AirfillAdmin(admin.ModelAdmin):
    pass
