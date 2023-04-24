from django.db import models

# Create your models here.
class equipment_repair(models.Model):
    name = models.CharField(max_length=100, help_text='First and Last Name')
    date_of_repair = models.DateField()
    equipment = (
        ('BCD', 'BCD'),
        ('Regulator', 'Regulator'),
        ('Wetsuit', 'Wetsuit'),
        ('Tank', 'Tank'),
        ('Weights', 'Weights'),
        ('Mask', 'Mask'),
        ('Fins', 'Fins'),
        ('Snorkel', 'Snorkel'),
        ('Dive Computer', 'Dive Computer'),
        ('Dive Light', 'Dive Light'),
        ('Dive Bag', 'Dive Bag'),
        ('Other', 'Other'),
    )
    equipment_repaired = models.CharField(max_length=100, choices=equipment)
    equipment_serial_number = models.CharField(max_length=100, blank=True, help_text='Serial Number')
    equipment_size = models.CharField(max_length=100, blank=True, help_text='Size')
    equipment_color = models.CharField(max_length=100, blank=True, help_text='Color')
    equipment_condition = (
        ('New', 'New'),
        ('Used', 'Used'),
    )
    equipment_condition = models.CharField(max_length=100, choices=equipment_condition)
    equipment_notes = models.CharField(max_length=100, blank=True, help_text='Notes')
    equipment_repair_price = models.IntegerField()
    equipment_deposit = models.IntegerField()
    equipment_repair_insurance = models.IntegerField()
    equipment_repair_insurance_price = models.IntegerField()
    equipment_repair_total = models.IntegerField()
    equipment_repair_payment = models.IntegerField()
    equipment_repair_payment_type = (
        ('Cash', 'Cash'),
        ('Check', 'Check'),
        ('Credit Card', 'Credit Card'),
        ('Debit Card', 'Debit Card'),
        ('Paypal', 'Paypal'),
        ('Venmo', 'Venmo'),
        ('Cash App', 'Cash App'),
        ('Zelle', 'Zelle'),
    )

    def __str__(self):
        return self.name