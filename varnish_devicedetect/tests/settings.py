import django
from os import path


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    },
}

INSTALLED_APPS = ['varnish_devicedetect']

MIDDLEWARE_CLASSES = (
    'varnish_devicedetect.middleware.DeviceDetectMiddleware',
)

ROOT_URLCONF = 'varnish_devicedetect.tests.urls'

if django.VERSION >= (1, 8):
    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                path.join(path.dirname(__file__), "templates"),
            ],
        },
    ]
else:
    TEMPLATE_DIRS = (
        path.join(path.dirname(__file__), "templates"),
    )

SECRET_KEY = 'varnish_devicedetect'
