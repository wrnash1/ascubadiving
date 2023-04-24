from django.db import models
from phone_field import PhoneField


# Create your models here.
class add_diver(models.Model):
    name = models.CharField(max_length=100, help_text='First and Last Name')
    certification_number = models.IntegerField()
    agency = (
        ('PADI', 'PADI'),
        ('NAUI', 'NAUI'),
        ('SSI', 'SSI'),
        ('BSAC', 'BSAC'),
        ('CMAS', 'CMAS'),
        ('SDI', 'SDI'),
        ('TDI', 'TDI'),
        ('IANTD', 'IANTD'),
        ('SDI', 'SDI'),
    )
    certification_agency = models.CharField(max_length=100, choices=agency)
    Date_of_birth = models.DateField()
    insurance = (
        ('Yes', 'Yes'),
        ('No', 'No'),
    )
    student_insurance = models.CharField(max_length=5, choices=insurance, help_text='Yes or No')
    dan_insurance = models.CharField(max_length=100, blank=True, help_text='Type in Dan Insurance Number')
    email = models.EmailField(max_length=100)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    address = models.CharField(max_length=100, help_text='Street Address')
    city = models.CharField(max_length=100, help_text='City')
    state = models.CharField(max_length=100, help_text='State')
    zip = models.IntegerField(help_text='Zip Code')
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Extra Extra Large'),
        ('XXXL', 'Extra Extra Extra Large'),
    )
    shirt_size = models.CharField(max_length=4, choices=SHIRT_SIZES)

    def __str__(self):
        return self.name
