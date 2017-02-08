from base import *

DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{cookiecutter.project_name}}',
        'HOST': '',
        'USER': '',
        'PASSWORD': '',
        'CONN_MAX_AGE': 600,
    }
}

TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'key_prefix'
    }
}

ALLOWED_HOSTS = ['.{{cookiecutter.domain_name}}', '{{cookiecutter.domain_name}}.'] # subdomains and FQDN

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'
