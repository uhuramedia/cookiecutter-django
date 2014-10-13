# -*- coding: utf-8 -*-
from base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{cookiecutter.project_name}}',
        'HOST': '',
        'USER': 'root',
        'PASSWORD': ''
    }
}

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

SECRET_KEY = '#'

LANGUAGE_CODE = 'en'