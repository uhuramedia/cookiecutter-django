# -*- coding: utf-8 -*-

import os
import datetime
from contextlib import contextmanager
from fabric.api import env, run, local, prefix, sudo


def live():
    """Connects to the server."""
    env.hosts = [os.environ.get('{{cookiecutter.repo_name}}_host')]
    env.user = 'freshmilk'
    env.cwd = '/var/www/{{cookiecutter.domain_name}}'
    env.connect_to = '{0}@{1}:{2}'.format(env.user, env.hosts[0], env.cwd)


def beta():
    """Connects to beta/testing server"""
    env.hosts = [os.environ.get('{{cookiecutter.repo_name}}_host')]
    env.user = 'freshmilk'
    env.cwd = '/var/www/beta.{{cookiecutter.domain_name}}'
    env.connect_to = '{0}@{1}:{2}'.format(env.user, env.hosts[0], env.cwd)


def gitpull(tag=None):
    """Pulls upstream branch on the server."""
    if tag is not None:
        run('git pull')
        run('git checkout %s' % tag)
    else:
        run('git pull')


@contextmanager
def source_env():
    """Actives embedded virtual env"""
    with prefix('source env/bin/activate'):
        yield


def collectstatic():
    """Collect static files on server."""
    with source_env():
        run('python manage.py collectstatic')


def migrate():
    """Sync project database on server."""
    with source_env():
        run('python manage.py migrate')


def touch():
    """Touch the wsgi file."""
    run('touch {{cookiecutter.repo_name}}/wsgi.py')


def update(tag=None):
    """Runs gitpull, develop, collectstatic, migrate and touch.
    """
    gitpull()
    collectstatic()
    migrate()
    touch()


def dump():
    run('python manage.py dumpdata > %s' datetime.datetime.now())


def sync_media():
    local('rsync -avzh -e ssh %s/../media/* ../media' % env.connect_to)


def sync_dump():
    local('rsync -avPhzL -e ssh %s/var/dump.sql.gz var' % env.connect_to)


def mirror():
    """Runs dump, sync_media, sync_dump and sqlimport."""
    dump()
    sync_media()
    sync_dump()
    local('python manage.py sqlimport')
