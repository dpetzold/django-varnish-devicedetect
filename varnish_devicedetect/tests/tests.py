from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.test import SimpleTestCase


class MiddlewareTest(SimpleTestCase):

    def test_middleware_assigns_user_agent(self):
        client = Client(HTTP_USER_AGENT=ipad_ua_string)
        response = client.get(reverse('user_agent_test'))
        self.assertIsInstance(response.context['user_agent'], UserAgent)
