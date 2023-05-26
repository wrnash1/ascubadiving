from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


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
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Certification"
        verbose_name_plural = "Certifications"


class Customer(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField()
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True)
    employee = models.BooleanField(default=False)
    picture = models.ImageField(upload_to="customer_images/", null=True, blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    emergency_contact_name = models.CharField(max_length=100)
    emergency_contact_phone = models.CharField(max_length=20)
    medical_conditions = models.TextField(default="NKDA")
    notes = models.TextField(default="None")
    shopify_user = models.ForeignKey(
        "ShopifyUser", on_delete=models.SET_NULL, null=True
    )  # Link to ShopifyUser model
    certifications = models.ManyToManyField(
        Certification,
        verbose_name="certifications",
        blank=True,
        related_name="customers",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"


class Airfill(models.Model):
    dive_details = models.CharField(max_length=200)
    gas_composition = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.dive_details

    class Meta:
        verbose_name = "Airfill"
        verbose_name_plural = "Airfills"


class Compressor(models.Model):
    shop_id = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    hours = models.PositiveIntegerField()

    def __str__(self):
        return self.shop_id

    class Meta:
        verbose_name = "Compressor"
        verbose_name_plural = "Compressors"


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Document"
        verbose_name_plural = "Documents"


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    rental_price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Equipment"
        verbose_name_plural = "Equipment"


class EquipmentRepair(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    issue_description = models.TextField()
    repair_status = models.CharField(max_length=100)
    repair_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Repair for {self.equipment.name} - {self.customer.name}"

    class Meta:
        verbose_name = "Equipment Repair"
        verbose_name_plural = "Equipment Repairs"


class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(
        Customer, through="CourseRegistration", related_name="courses_enrolled"
    )
    instructors = models.ManyToManyField(Customer, related_name="courses_instructed")
    divemaster = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="courses_divemastered"
    )
    google_calendar_url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class CourseRegistration(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f"Registration for {self.course.name} - {self.customer.name}"

    class Meta:
        verbose_name = "Course Registration"
        verbose_name_plural = "Course Registrations"


class Trip(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date = models.DateField()
    participants = models.ManyToManyField(Customer)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"


class StaffSchedule(models.Model):
    staff_member = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Schedule for {self.staff_member.name} - {self.date}"

    class Meta:
        verbose_name = "Staff Schedule"
        verbose_name_plural = "Staff Schedules"


class ShopifyUser(models.Model):
    shopify_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Shopify User"
        verbose_name_plural = "Shopify Users"


class Company(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
