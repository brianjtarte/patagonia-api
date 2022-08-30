from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Campsite


class CampsiteTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_camp = Campsite.objects.create(author=test_user, title="Campsite1", body="A campsite")
        test_camp.save()

    def test_campsites_model(self):
        campsite = Campsite.objects.get(id=1)
        actual_author = str(campsite.author)
        actual_title = str(campsite.title)
        actual_body = str(campsite.body)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_title, "Campsite1")
        self.assertEqual(actual_body, "A campsite")