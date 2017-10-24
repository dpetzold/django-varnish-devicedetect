from . models import Device


def simple_middleware(get_response):

    def middleware(request):

        device = Device(request.META.get('X-UA-Device', 'none'))
        if not hasattr(request, 'device'):
            request.device = device

        response = get_response(request)
        return response

    return middleware
