from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import Compressor, MaintenanceAlert


@receiver(post_save, sender=Compressor)
def check_air_filters(sender, instance, created, **kwargs):
    if created:
        # Check if air filters need to be changed
        if instance.minutes == 900:
            # Create a maintenance alert for changing air filters
            MaintenanceAlert.objects.create(
                compressor=instance,
                alert_type=MaintenanceAlert.AIR_FILTERS,
                alert_date=timezone.now(),
            )


@receiver(post_save, sender=Compressor)
def check_oil_change(sender, instance, created, **kwargs):
    if created:
        # Check if oil needs to be changed
        if instance.minutes == 3000:
            # Create a maintenance alert for changing oil
            MaintenanceAlert.objects.create(
                compressor=instance,
                alert_type=MaintenanceAlert.OIL_CHANGE,
                alert_date=timezone.now(),
            )
