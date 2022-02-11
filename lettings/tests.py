# Create your tests here.
from django.test import Client, TestCase
from django.urls import reverse

from lettings.models import Address, Letting


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.address = Address.objects.create(
            number=1,
            street="Fake street",
            city="Fake city",
            state="Fake state",
            zip_code="12345",
            country_iso_code="AZE",
        )
        self.letting = Letting.objects.create(title="Fake title", address=self.address)

    def test_lettings_homepage(self):
        response = self.client.get(reverse("lettings:index"))

        self.assertContains(response, "<title>Lettings</title>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/index.html")

    def test_lettings_title(self):
        response = self.client.get(reverse("lettings:letting", args=[self.letting.id]))

        self.assertContains(response, "<title>Fake title</title>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "lettings/letting.html")
