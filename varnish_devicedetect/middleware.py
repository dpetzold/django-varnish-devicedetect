from django.utils.deprecation import MiddlewareMixin

from .models import Device
from .settings import (
    HTTP_HEADER,
    REQUEST_ATTR,
)


class DeviceDetectMiddleware(MiddlewareMixin):

    def process_request(self, request):
        device = Device(request.META.get(HTTP_HEADER, 'pc'))
        if not hasattr(request, REQUEST_ATTR):
            setattr(request, REQUEST_ATTR, device)
