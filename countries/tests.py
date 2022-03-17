from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Country

class CountryTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = get_user_model().objects.create_user(username='testuser', password='pass')
        testuser1.save()

        test_thing = Country.objects.create(name='rake', organization=testuser1, continent='Better for collecting leaves than a shovel.')
        test_thing.save()

    def test_things_model(self):
        thing = Country.objects.get(id=1)
        actual_owner = str(thing.organization)
        actual_name = str(thing.name)
        actual_description = str(thing.continent)
        self.assertEqual(actual_owner,'testuser')
        self.assertEqual(actual_name, 'rake')
        self.assertEqual(actual_description,'Better for collecting leaves than a shovel.')
