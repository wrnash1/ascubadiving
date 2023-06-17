from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from diveshopmanagement.models import Organization


class Command(BaseCommand):
    def handle(self, *args, **options):
        Organization.objects.bulk_create(
            [
                Organization(name="PADI"),
                Organization(name="NAUI"),
                Organization(name="SSI"),
                Organization(name="SDI"),
                Organization(name="CMAS"),
                Organization(name="BSAC"),
                Organization(name="ACUC"),
                Organization(name="RAID"),
                Organization(name="IANTD"),
                Organization(name="GUE"),
                Organization(name="TDI"),
                Organization(name="HSA"),
                Organization(name="YMCA"),
                Organization(name="SEI"),
                Organization(name="PDIC"),
                Organization(name="NASE"),
                Organization(name="SAA"),
                Organization(name="IADS"),
                Organization(name="CRESSI"),
                Organization(name="SSI"),
                Organization(name="TDI"),
                Organization(name="IANTD"),
                Organization(name="GUE"),
                Organization(name="NAUI"),
                Organization(name="CMAS"),
                Organization(name="ACUC"),
                Organization(name="RAID"),
                Organization(name="PDIC"),
                Organization(name="SAA"),
                Organization(name="IADS"),
                Organization(name="SEI"),
                Organization(name="YMCA"),
                Organization(name="SDI"),
                Organization(name="BSAC"),
                Organization(name="HSA"),
                Organization(name="NASE"),
                Organization(name="CRESSI"),
                Organization(name="IANTD"),
                Organization(name="PADI"),
                Organization(name="GUE"),
            ]
        )

        User = get_user_model()
        admin_user = User.objects.filter(is_superuser=True).first()
        if admin_user:
            organizations = Organization.objects.all()
            admin_user.organization = organizations.first()
            admin_user.save()

        self.stdout.write(self.style.SUCCESS("Successfully populated organizations."))

