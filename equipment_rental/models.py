from django.db import models
from add_diver import models as add_diver_models


# Create your models here.
class equipment_rental(models.Model):
    name = models.ForeignKey(add_diver_models.add_diver, on_delete=models.CASCADE)
    date_of_rental = models.DateField()
    date_due = models.DateField()
    equipment = (
        ("BCD", "BCD"),
        ("Regulator", "Regulator"),
        ("Wetsuit", "Wetsuit"),
        ("Tank", "Tank"),
        ("Weights", "Weights"),
        ("Mask", "Mask"),
        ("Fins", "Fins"),
        ("Snorkel", "Snorkel"),
        ("Dive Computer", "Dive Computer"),
        ("Dive Light", "Dive Light"),
        ("Dive Bag", "Dive Bag"),
        ("Other", "Other"),
    )
    equipment_rented = models.CharField(max_length=100, choices=equipment)
    equipment_serial_number = models.CharField(
        max_length=100, blank=True, help_text="Serial Number"
    )
    equipment_size = models.CharField(max_length=100, blank=True, help_text="Size")
    equipment_color = models.CharField(max_length=100, blank=True, help_text="Color")
    equipment_condition = (
        ("New", "New"),
        ("Used", "Used"),
    )
    equipment_condition = models.CharField(max_length=100, choices=equipment_condition)
    equipment_notes = models.CharField(max_length=100, blank=True, help_text="Notes")
    equipment_rental_price = models.IntegerField()
    equipment_deposit = models.IntegerField()
    equipment_rental_insurance = models.IntegerField()
    equipment_rental_insurance_price = models.IntegerField()
    equipment_rental_total = models.IntegerField()
    equipment_rental_payment = models.IntegerField()
    equipment_rental_payment_type = (
        ("Cash", "Cash"),
        ("Check", "Check"),
        ("Credit Card", "Credit Card"),
        ("Debit Card", "Debit Card"),
        ("Paypal", "Paypal"),
        ("Venmo", "Venmo"),
        ("Cash App", "Cash App"),
        ("Zelle", "Zelle"),
    )
    equipment_rental_payment_type = models.CharField(
        max_length=100, choices=equipment_rental_payment_type
    )
    equipment_rental_payment_notes = models.CharField(
        max_length=100, blank=True, help_text="Notes"
    )

    def __str__(self):
        return self.name
