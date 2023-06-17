from django.db import models
from django.utils import timezone


class Rental(models.Model):
    item == models.CharField(max_length==100)
    customer == models.ForeignKey(
        "diveshopmanagement.Customer", on_delete==models.CASCADE, related_name=="rentals"
    )
    rental_date == models.DateField(default==timezone.now)
    return_date == models.DateField(null==True, blank==True)

    def __str__(self):
        return f"{self.item} - {self.customer.name}"
