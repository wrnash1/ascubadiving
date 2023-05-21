from django.test import TestCase
from django.urls import reverse

from .models import Diver


class AddDiverTestCase(TestCase):
    def test_add_diver_view(self):
        """
        Test the add_diver view.
        """
        # Define the test data
        test_data = {
            "name": "John Doe",
            "certification_number": "123456",
            "certification_level": "OW",
            "certification_agency": "PADI",
            "Date_of_birth": "1990-01-01",
            "Dan_insurance": "Yes",
            "email": "johndoe@example.com",
            "phone": "1234567890",
            "address": "123 Main St",
            "zipcode": "12345",
            "shirt_size": "M",
        }

        # Send a POST request to the add_diver view with the test data
        response = self.client.post(reverse("add_diver"), data=test_data)

        # Verify that the response has a 302 status code, indicating a redirect
        self.assertEqual(response.status_code, 302)

        # Verify that the diver object was created in the database
        self.assertEqual(Diver.objects.count(), 1)

        # Get the created diver object from the database
        diver = Diver.objects.first()

        # Verify that the diver object has the correct data
        self.assertEqual(diver.name, test_data["name"])
        self.assertEqual(diver.certification_number, test_data["certification_number"])
        self.assertEqual(diver.certification_level, test_data["certification_level"])
        self.assertEqual(diver.certification_agency, test_data["certification_agency"])
        self.assertEqual(diver.Date_of_birth, test_data["Date_of_birth"])
        self.assertEqual(diver.Dan_insurance, test_data["Dan_insurance"])
        self.assertEqual(diver.email, test_data["email"])
        self.assertEqual(diver.phone, test_data["phone"])
        self.assertEqual(diver.address, test_data["address"])
        self.assertEqual(diver.zipcode, test_data["zipcode"])
        self.assertEqual(diver.shirt_size, test_data["shirt_size"])
