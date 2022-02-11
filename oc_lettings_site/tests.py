from django.test import Client, TestCase
from django.urls import reverse


class TestView(TestCase):
    def test_homepage_success(self):
        client = Client()
        response = client.get(reverse("index"))
        
        self.assertContains(response, "<title>Holiday Homes</title>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
