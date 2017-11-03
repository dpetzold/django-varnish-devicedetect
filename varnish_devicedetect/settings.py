from django.conf import settings

REQUEST_ATTR = getattr(settings, 'VARNISH_DEVICEDETECT_REQUEST_ATTR', 'device')
HTTP_HEADER = getattr(settings, 'VARNISH_DEVICEDETECT_HTTP_HEADER', 'HTTP_X_UA_DEVICe')
