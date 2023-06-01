from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

# Rest of the code...


class User(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="groups",
        blank=True,
        related_name="diveshopmanagement_users",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="user permissions",
        blank=True,
        related_name="diveshopmanagement_users",
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
    customer = models.ForeignKey(
        "diveshopmanagement.Customer",
        on_delete=models.CASCADE,
        related_name="certifications",
    )
    certification_agency = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()

    def __str__(self):
        return f"{self.customer.name} - {self.certification_agency}"

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"


class Level(models.Model):
    name = models.CharField(max_length=100)  # Add a field for the level name

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

    def __str__(self):
        return self.name


class Customer(models.Model):
    T_SHIRT_SIZES = (
        ("S", "Small"),
        ("M", "Medium"),
        ("L", "Large"),
        ("XL", "Extra Large"),
        ("XXL", "Extra Extra Large"),
    )

    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to="customer_images/", null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    birthdate = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    certification_level = models.CharField(
        max_length=50, choices=Level.CERTIFICATION_LEVELS
    )
    t_shirt_size = models.CharField(max_length=10, choices=T_SHIRT_SIZES)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.name

    employee = models.BooleanField(default=False)
    emergency_contact_name = models.CharField(max_length=100, null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=20, null=True, blank=True)
    medical_conditions = models.TextField(blank=True)
    dan_insurance = models.BooleanField(default=False)
    dan_insurance_number = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.get_certification_level_display()


class DiveShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class GasComposition(models.Model):
    gas_type = models.CharField(max_length=100)
    oxygen_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.gas_type


class Tank(models.Model):
    tank_identifier = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    hydro_dropoff_date = models.DateField(null=True, blank=True)
    hydro_pickup_date = models.DateField(null=True, blank=True)
    hydro_passed = models.BooleanField(default=False)

    def __str__(self):
        return self.tank_identifier


class Airfill(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    fill_pressure = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    oxygen_percentage = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.tank} - {self.date}"


class GasBlending(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    gas_composition = models.ForeignKey(GasComposition, on_delete=models.CASCADE)
    blending_method = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.tank} - {self.gas_composition}"


class HydrostaticTest(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    dropoff_date = models.DateField()
    pickup_date = models.DateField(null=True, blank=True)
    result = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tank} - {self.dropoff_date}"


class TankInventory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.tank} - {self.status}"
