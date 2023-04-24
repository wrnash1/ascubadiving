from django.db import models


# Create your models here.
class airfill(models.Model):
    name = models.CharField(max_length=100)
    tank_serial_number = models.CharField(max_length=100)
    visual_date = models.IntegerField()
    hydro_date = models.IntegerField()

    def __str__(self):
        return self.name
