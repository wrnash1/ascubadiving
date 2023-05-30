from django.contrib import admin
from diveshopmanagement.models import Customer, Organization, Certification


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthdate",
        "get_organization",
        "get_level",
        "t_shirt_size",
        "notes",
    )
    list_filter = ("organization__name", "level__certification_level")
    search_fields = ("name",)

    def get_organization(self, obj):
        return obj.organization.name if obj.organization else None

    get_organization.short_description = "Organization"

    def get_level(self, obj):
        return obj.level.certification_level if obj.level else None

    get_level.short_description = "Level"


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ("diver", "certification_level", "certification_agency")
    list_filter = ("certification_agency",)
    search_fields = ("diver__username",)

    def diver(self, obj):
        return obj.diver.username


admin.site.site_header = "Dive Shop Management Admin"
admin.site.site_title = "Dive Shop Management"
