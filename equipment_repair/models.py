from django.db import models
from add_diver import models as add_diver_models


# Create your models here.
class equipment_repair(models.Model):
    name = models.ForeignKey(add_diver_models.add_diver, on_delete=models.CASCADE)
    date_of_repair = models.DateField()
    equipment = (
        ("BCD", "BCD"),
        ("Regulator", "Regulator"),
        ("Wetsuit", "Wetsuit"),
        ("Dive Computer", "Dive Computer"),
        ("Other", "Other"),
        ("Poseidon", "Poseidon"),
        ("full face mask", "full face mask"),
    )
    equipment_repaired = models.CharField(max_length=100, choices=equipment)
    equipment_serial_number = models.CharField(
        max_length=100, blank=True, help_text="Serial Number"
    )

    quote = models.BooleanField(
        default=False, help_text="Do you need a Quote before we begin service?"
    )
    computer_battery_service = models.BooleanField(
        default=False, help_text="Computer Battery Service"
    )
    mouthpieces_changed = models.BooleanField(
        default=False, help_text="May we change bad mouthpieces?"
    )
    SPG_spool_service = models.BooleanField(
        default=False, help_text="May we change bad SPG spool I-rings?"
    )
    bad_hoses = models.BooleanField(default=False, help_text="May we change bad hoses?")
    Customer_notes = models.TextField(blank=True, help_text="Customer Notes")
    Technician_notes = models.TextField(blank=True, help_text="Technician Notes")
    date_of_pickup = models.DateField(blank=True, null=True)
    date_of_dropoff = models.DateField(blank=True, null=True)
    date_mailed = models.DateField(blank=True, null=True)
    tracking_number = models.CharField(
        max_length=100, blank=True, help_text="Tracking Number"
    )

    def __str__(self):
        return self.name
