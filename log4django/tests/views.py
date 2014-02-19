from django.core.urlresolvers import reverse
from django.test import TestCase

from . import TEST_USERNAME, TEST_PASSWORD


class MainScreenTest(TestCase):

    def setUp(self):
        self.client.login(username=TEST_USERNAME, password=TEST_PASSWORD)

    def test_context(self):
        response = self.client.get(reverse('log4django:logrecord_list'))
        self.assertIn('records', response.context)
        self.assertIn('apps', response.context)
        self.assertIn('loggers', response.context)
        self.assertIn('levels', response.context)
        self.assertIn('filter_levels', response.context)
