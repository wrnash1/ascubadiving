from django.contrib import admin
from .models import Gas, Blend, BlendComponent


@admin.register(Gas)
class GasAdmin(admin.ModelAdmin):
    list_display = ("name", "oxygen_percentage", "helium_percentage")


@admin.register(Blend)
class BlendAdmin(admin.ModelAdmin):
    list_display = ("name",)


@admin.register(BlendComponent)
class BlendComponentAdmin(admin.ModelAdmin):
    list_display = ("gas", "blend", "percentage")
