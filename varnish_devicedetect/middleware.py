from django.utils.deprecation import MiddlewareMixin
from . models import Device


class DeviceDetectMiddleware(MiddlewareMixin):

    def process_request(self, request):

        device = Device(request.META.get('X-UA-Device', 'none'))
        if not hasattr(request, 'device'):
            request.device = device
