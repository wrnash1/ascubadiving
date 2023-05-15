from django.db import models
from add_diver.models import Diver


class airfill(models.Model):
    name = models.ForeignKey(Diver, on_delete=models.CASCADE)
    tank_serial_number = models.CharField(max_length=100)
    visual_date = models.IntegerField()
    hydro_date = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.tank_serial_number}"
