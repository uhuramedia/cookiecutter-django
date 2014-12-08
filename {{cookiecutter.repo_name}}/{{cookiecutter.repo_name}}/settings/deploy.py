from base import *

DEBUG = False

TEMPLATE_DEBUG = DEBUG


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{cookiecutter.project_name}}',
        'HOST': '',
        'USER': '',
        'PASSWORD': ''
    }
}

TEMPLATE_LOADERS = (
    (
        'django.template.loaders.cached.Loader', (
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        )
    ),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'key_prefix'
    }
}

ALLOWED_HOSTS = ['.{{cookiecutter.domain_name}}', '{{cookiecutter.domain_name}}.'] # subdomains and FQDN

ROOT_URLCONF = '{{cookiecutter.repo_name}}.urls'