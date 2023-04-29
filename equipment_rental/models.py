from django.db import models
from add_diver import models as add_diver_models


class Equipment(models.Model):
    name = models.CharField(max_length=100)
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

    def __str__(self):
        return f"{self.name} ({self.serial_number})"


class Rental(models.Model):
    diver = models.ForeignKey(add_diver_models.add_diver, on_delete=models.CASCADE)
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
