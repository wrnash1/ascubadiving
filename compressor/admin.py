from django.contrib import admin
from .models import Compressor


@admin.register(Compressor)
class CompressorAdmin(admin.ModelAdmin):
    list_display = ("name", "hours", "last_filter_change", "last_oil_change")
