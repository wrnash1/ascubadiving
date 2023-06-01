from django.contrib import admin
from diveshopmanagement.models import Customer, Organization, Certification


class CertificationInline(admin.TabularInline):
    model = Certification
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "birthdate",
        "get_organization",
        "get_level",
        "t_shirt_size",
        "notes",
    )
    list_filter = ("organization__name", "certification_level")
    search_fields = ("name",)

    def get_organization(self, obj):
        return obj.organization.name if obj.organization else None

    get_organization.short_description = "Organization"

    def get_level(self, obj):
        return obj.level.certification_level if obj.level else None

    get_level.short_description = "Level"

    inlines = [CertificationInline]


class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ("diver", "get_certification_level", "certification_agency")
    list_filter = ("certification_agency",)
    search_fields = ("diver__username",)

    def diver(self, obj):
        return obj.diver.username

    def get_certification_level(self, obj):
        return obj.diver.level.certification_level if obj.diver.level else None

    get_certification_level.short_description = "Certification Level"


admin.site.register(Customer, CustomerAdmin)
admin.site.register(Organization, OrganizationAdmin)
admin.site.register(Certification, CertificationAdmin)

admin.site.site_header = "Dive Shop Management Admin"
admin.site.site_title = "Dive Shop Management"
