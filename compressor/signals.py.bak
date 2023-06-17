from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from diveshopmanagement.models import Compressor, MaintenanceAlert

@receiver(post_save, sender=Compressor)
def check_air_filters(sender, instance, created, **kwargs):
    if created and instance.check_air_filter_alert():
        MaintenanceAlert.objects.create(
            compressor=instance,
            alert_type=MaintenanceAlert.AIR_FILTERS,
            alert_date=timezone.now(),
        )

@receiver(post_save, sender=Compressor)
def check_oil_change(sender, instance, created, **kwargs):
    if created and instance.check_oil_change_alert():
        MaintenanceAlert.objects.create(
            compressor=instance,
            alert_type=MaintenanceAlert.OIL_CHANGE,
            alert_date=timezone.now(),
        )