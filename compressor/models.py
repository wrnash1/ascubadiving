from django.db import models

class Compressor(models.Model):
    minutes = models.IntegerField(default=0)
    date_turned_on = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"Compressor ({self.id})"

    def check_air_filter_alert(self):
        if self.minutes >= 900:
            return True
        return False

    def reset_air_filter(self):
        self.minutes = 0
        self.save()

    def check_oil_change_alert(self):
        if self.minutes >= 3000:
            return True
        return False

    def reset_oil_change(self):
        self.minutes = 0
        self.save()
        
class Compressor(models.Model):
    start_time = models.DateTimeField(null=True, blank=True)
    minutes = models.IntegerField(default=0)
    notes = models.TextField(blank=True)