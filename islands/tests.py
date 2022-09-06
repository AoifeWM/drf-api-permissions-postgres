from django.test import TestCase

from django.test import TestCase
from django.contrib.auth import get_user_model

from .models import Island


class IslandTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = get_user_model().objects.create_user(username='test_user', password='pass')
        test_user.save()

        test_thing = Island.objects.create(name="Bermuda", ocean="Atlantic Ocean", description="An island with a spooky patch of sea named after it.", size="54 square kilometres", contributor=test_user,)
        test_thing.save()

    def test_things_model(self):
        thing = Island.objects.get(id=1)
        actual_author = str(thing.contributor)
        actual_name = str(thing.name)
        actual_description = str(thing.description)
        self.assertEqual(actual_author, "test_user")
        self.assertEqual(actual_name, "Bermuda")
        self.assertEqual(actual_description, "An island with a spooky patch of sea named after it.")
