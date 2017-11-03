from mock import Mock

from django.test import SimpleTestCase

from varnish_devicedetect.models import Device
from varnish_devicedetect.middleware import DeviceDetectMiddleware
from varnish_devicedetect.settings import HTTP_HEADER


class MiddlewareTest(SimpleTestCase):

    def setUp(self):
        self.ddm = DeviceDetectMiddleware()
        self.request = Mock(spec='META')
        self.request.META = {}

    def test_middleware_device_pc(self):

        self.request.META[HTTP_HEADER] = 'pc'
        self.assertEqual(self.ddm.process_request(self.request), None)
        self.assertIsInstance(self.request.device, Device)
        self.assertEqual(str(self.request.device), 'pc')
        self.assertTrue(self.request.device.is_pc)

    def test_middleware_device_mobile(self):

        self.request.META[HTTP_HEADER] = 'mobile-android'
        self.assertEqual(self.ddm.process_request(self.request), None)
        self.assertEqual(str(self.request.device), 'mobile-android')
        self.assertFalse(self.request.device.noattr)
        self.assertFalse(self.request.device.is_pc)
        self.assertTrue(self.request.device.mobile_android)
        self.assertTrue(self.request.device.is_mobile)
        self.assertTrue(self.request.device.is_android)

    def test_middleware_device_tablet(self):

        self.request.META[HTTP_HEADER] = 'tablet-android'
        self.assertEqual(self.ddm.process_request(self.request), None)
        self.assertEqual(str(self.request.device), 'tablet-android')
        self.assertFalse(self.request.device.noattr)
        self.assertFalse(self.request.device.is_pc)
        self.assertFalse(self.request.device.is_mobile)
        self.assertTrue(self.request.device.tablet_android)
        self.assertTrue(self.request.device.is_android)
        self.assertTrue(self.request.device.is_tablet)
