from django.db import models

class Gas(models.Model):
    name = models.CharField(max_length=100)
    oxygen_percentage = models.FloatField()
    helium_percentage = models.FloatField()

    def __str__(self):
        return self.name

class Blend(models.Model):
    name = models.CharField(max_length=100)
    gases = models.ManyToManyField(Gas, through='BlendComponent')

    def __str__(self):
        return self.name

class BlendComponent(models.Model):
    gas = models.ForeignKey(Gas, on_delete=models.CASCADE)
    blend = models.ForeignKey(Blend, on_delete=models.CASCADE)
    percentage = models.FloatField()

    def __str__(self):
        return f"{self.gas} - {self.percentage}%"
