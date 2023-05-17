from django.db import models
from add_diver.models import Diver


class Equipment(models.Model):
    EQUIPMENT_CHOICES = [
        ("regulator", "Regulator"),
        ("regulator_console", "Regulator with Console"),
        ("regulator_computer", "Regulator with Computer"),
        ("sidemount_rig", "Sidemount Rig/Mount"),
        ("bcd", "BCD"),
        ("rebreather", "Rebreather"),
        ("exposure_suit", "Exposure Suit"),
        ("dry_suit", "Dry Suit"),
        ("dive_skin", "Dive Skin"),
        ("hood", "Hood"),
        ("mask", "Mask"),
        ("snorkel", "Snorkel"),
        ("fins", "Fins"),
        ("boots", "Boots"),
        ("gloves", "Gloves"),
        ("weights", "Weights"),
        ("weight_belt", "Weight Belt"),
        ("light", "Light"),
        ("camera_video", "Camera/Video"),
        ("other", "Other"),
    ]

    name = models.CharField(max_length=100, choices=EQUIPMENT_CHOICES)
    quantity = models.IntegerField(default=1)
    serial_number = models.CharField(
        max_length=100, blank=True, help_text="Serial Number"
    )
    size = models.CharField(max_length=100, blank=True, help_text="Size")
    color = models.CharField(max_length=100, blank=True, help_text="Color")
    condition_choices = (
        ("New", "New"),
        ("Used", "Used"),
    )
    condition = models.CharField(max_length=100, choices=condition_choices)
    notes = models.CharField(max_length=100, blank=True, help_text="Notes")
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class Rental(models.Model):
    diver = models.ForeignKey(Diver, on_delete=models.CASCADE)
    date_of_rental = models.DateField()
    date_due = models.DateField()
    equipment_rental = models.ManyToManyField(Equipment, through="RentalEquipment")

    def __str__(self):
        return f"{self.diver.name} - Rental #{self.id}"


class RentalEquipment(models.Model):
    rental = models.ForeignKey(Rental, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    rental_price = models.IntegerField()
    deposit = models.IntegerField()
    rental_insurance = models.IntegerField()
    rental_insurance_price = models.IntegerField()
    rental_total = models.IntegerField()

    def __str__(self):
        return f"{self.rental} - {self.equipment}"
