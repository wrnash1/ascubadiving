from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# accounts section


class User(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        verbose_name="groups",
        blank=True,
        related_name="diveshopmanagement_user_set",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name="user permissions",
        blank=True,
        related_name="diveshopmanagement_user_set",
    )

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"


class Organization(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Organization"
        verbose_name_plural = "Organizations"


class Certification(models.Model):
    diver = models.ForeignKey(User, on_delete=models.CASCADE)
    certification_level = models.CharField(max_length=100)
    certification_agency = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.diver.username} - {self.certification_level}"

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"


class Level(models.Model):
    CERTIFICATION_LEVELS = (
        ("OW", "Open Water"),
        ("AOW", "Advanced Open Water"),
        ("RD", "Rescue Diver"),
        ("DM", "Dive Master"),
        ("AI", "Assistant Instructor"),
        ("OWSI", "Open Water Scuba Instructor"),
        ("MSDT", "Master Scuba Diver Trainer"),
        ("IDC", "Instructor Development Course"),
        ("IE", "Instructor Examination"),
        ("MI", "Master Instructor"),
        ("CD", "Course Director"),
        ("IT", "Instructor Trainer"),
        ("CIT", "Course Director Trainer"),
    )

    certification_level = models.CharField(max_length=50, choices=CERTIFICATION_LEVELS)

    def __str__(self):
        return self.get_certification_level_display()

    employee = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="customer_images/", null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, null=True, blank=True)
    medical_conditions = models.TextField(blank=True)
    dan_insurance = models.BooleanField(default=False)
    dan_insurance_number = models.CharField(max_length=100, null=True, blank=True)


class Customer(models.Model):
    T_SHIRT_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "Extra Extra Large"),
    )

    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    t_shirt_size = models.CharField(max_length=10, choices=T_SHIRT_SIZES)
    notes = models.TextField(blank=True)
    # Add any other relevant fields for customer information

    def __str__(self):
        return self.name


# Dive shop name for template.


class DiveShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # Add any other relevant fields for dive shop


# Airfills Sections


class GasComposition(models.Model):
    gas_type = models.CharField(max_length=100)
    oxygen_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    # Add any other relevant fields for gas composition


class Tank(models.Model):
    tank_identifier = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hydro_dropoff_date = models.DateField(null=True, blank=True)
    hydro_pickup_date = models.DateField(null=True, blank=True)
    hydro_passed = models.BooleanField(default=False)
    # Add any other relevant fields for tank tracking


class Airfill(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    fill_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    oxygen_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    # Add any other relevant fields for airfills


class GasBlending(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    gas_composition = models.ForeignKey(GasComposition, on_delete=models.CASCADE)
    blending_method = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    # Add any other relevant fields for gas blending operations


class HydrostaticTest(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    dropoff_date = models.DateField()
    pickup_date = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=100)
    # Add any other relevant fields for hydrostatic testing


class TankInventory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)
    # Add any other relevant fields for tank inventory management
