from django.db import models
from add_diver import models as add_diver_models


# Create your models here.
class airfill(models.Model):
    #   name = models.CharField(max_length=100)
    name = models.ForeignKey(add_diver_models.add_diver, on_delete=models.CASCADE)
    tank_serial_number = models.CharField(max_length=100)
    visual_date = models.IntegerField()
    hydro_date = models.IntegerField()

def __str__(self):
    return f"{self.name} - {self.tank_serial_number}"

