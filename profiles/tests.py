# Create your tests here.
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from profiles.models import Profile


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.test_user = User.objects.create(username="Testuser")
        self.profile = Profile.objects.create(
            user=self.test_user, favorite_city="Paris"
        )

    def test_profile_homepage(self):
        response = self.client.get(reverse("profiles:index"))

        self.assertContains(response, "<title>Profiles</title>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/index.html")

    def test_user_profile(self):
        response = self.client.get(
            reverse("profiles:profile", args=[self.test_user.username])
        )

        self.assertContains(response, "<title>Testuser</title>")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile.html")
