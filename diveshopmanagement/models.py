from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


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
    # Add any other relevant fields for customer information


class Equipment(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add any other relevant fields for equipment details


class EquipmentInventory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length=100)
    # Add any other relevant fields for equipment inventory management


class DiveSite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    coordinates = models.CharField(max_length=100)
    water_conditions = models.CharField(max_length=100)
    # Add any other relevant fields for dive site information


class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add any other relevant fields for course details

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"


class Divemaster(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Divemaster"
        verbose_name_plural = "Divemasters"


class Dive(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)


class DiveContact(models.Model):
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)
    contact_type = models.CharField(max_length=100)
    contact_details = models.TextField()


class Trip(models.Model):
    name = models.CharField(max_length=100)
    # Add any other relevant fields for trip details

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Trip"
        verbose_name_plural = "Trips"


class StaffSchedule(models.Model):
    staff = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any other relevant fields for staff schedule


class DiveLog(models.Model):
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)
    date = models.DateField()
    duration = models.DurationField()
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    location = models.ForeignKey(DiveSite, on_delete=models.CASCADE)
    # Add any other relevant fields for dive log


class RentalEquipment(models.Model):
    dive = models.ForeignKey(Dive, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    # Add any other relevant fields for rental equipment


class RepairRequest(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=100)
    # Add any other relevant fields for repair request


class RepairUpdate(models.Model):
    repair_request = models.ForeignKey(RepairRequest, on_delete=models.CASCADE)
    update_date = models.DateField()
    update_description = models.TextField()
    # Add any other relevant fields for repair update


class Document(models.Model):
    name = models.CharField(max_length=100)
    file = models.FileField(upload_to="documents/")
    # Add any other relevant fields for document


class CourseSchedule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    # Add any other relevant fields for course schedule


class CourseStudent(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    # Add any other relevant fields for course student


class CourseInstructor(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    # Add any other relevant fields for course instructor


class CourseDivemaster(models.Model):
    course_schedule = models.ForeignKey(CourseSchedule, on_delete=models.CASCADE)
    divemaster = models.ForeignKey(Divemaster, on_delete=models.CASCADE)
    # Add any other relevant fields for course divemaster


class TripParticipant(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    participant = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any other relevant fields for trip participant


class StaffSchedule(models.Model):
    staff_member = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # Add any other relevant fields for staff schedule


class Certification(models.Model):
    diver = models.ForeignKey(User, on_delete=models.CASCADE)
    level = models.CharField(max_length=100)
    agency = models.CharField(max_length=100)
    issue_date = models.DateField()
    expiration_date = models.DateField()
    # Add any other relevant fields for certification


class EquipmentInventory(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    availability = models.BooleanField(default=True)
    quantity = models.PositiveIntegerField()
    condition = models.CharField(max_length=100)
    # Add any other relevant fields for equipment inventory


class DiveSite(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    coordinates = models.CharField(max_length=100)
    water_conditions = models.TextField()
    # Add any other relevant fields for dive site


class DiveLog(models.Model):
    diver = models.ForeignKey(User, on_delete=models.CASCADE)
    dive_site = models.ForeignKey(DiveSite, on_delete=models.CASCADE)
    date = models.DateField()
    depth = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DurationField()
    # Add any other relevant fields for dive log


class DiveCondition(models.Model):
    dive_log = models.ForeignKey(DiveLog, on_delete=models.CASCADE)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    visibility = models.DecimalField(max_digits=5, decimal_places=2)
    current = models.CharField(max_length=100)
    # Add any other relevant fields for dive condition


class DiveBuddy(models.Model):
    dive_log = models.ForeignKey(DiveLog, on_delete=models.CASCADE)
    buddy = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add any other relevant fields for dive buddy


class DivePhoto(models.Model):
    dive_log = models.ForeignKey(DiveLog, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="dive_photos/")
    caption = models.CharField(max_length=100)
    # Add any other relevant fields for dive photo


class DiveNote(models.Model):
    dive_log = models.ForeignKey(DiveLog, on_delete=models.CASCADE)
    note = models.TextField()
    # Add any other relevant fields for dive note


class DiveShop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    # Add any other relevant fields for dive shop


class RentalTransaction(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    rental_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    # Add any other relevant fields for rental transaction


class SalesTransaction(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    sale_date = models.DateField()
    # Add any other relevant fields for sales transaction


class Invoice(models.Model):
    transaction = models.ForeignKey(SalesTransaction, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    paid = models.BooleanField(default=False)
    # Add any other relevant fields for invoice
