from django.test import TestCase
from django.urls import reverse
from .models import Airfill


class AirfillTests(TestCase):
    def setUp(self):
        self.airfill = Airfill.objects.create(
            date="2023-05-01", fill_pressure=3000, oxygen_percentage=32.5
        )

    def test_airfill_list_view(self):
        url = reverse("airfills:airfill_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.airfill.date)

    def test_airfill_detail_view(self):
        url = reverse("airfills:airfill_detail", args=[self.airfill.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.airfill.fill_pressure)

    # Add more test cases as needed
