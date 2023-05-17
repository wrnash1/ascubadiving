from django.db import models

class Compressor(models.Model):
    name = models.CharField(max_length=100)
    hours = models.IntegerField()
    last_filter_change = models.DateField()
    last_oil_change = models.DateField()

    def __str__(self):
        return self.name
