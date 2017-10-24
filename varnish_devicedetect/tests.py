from django.core.urlresolvers import reverse
from django.http import HttpRequest
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.test import TestCase

from varnish_devicedetect.models import Device
from varnish_devicedetect.middleware import DeviceDetectMiddleware


class MiddlewareTest(TestCase):

    def setUp(self):
        self.middleware = DeviceDetectMiddleware()
        self.request = HttpRequest()

    def test_middleware_assigns_device(self):

        self.middleware.process_request(self.request)
        self.assertIsNotNone(self.request.device)
