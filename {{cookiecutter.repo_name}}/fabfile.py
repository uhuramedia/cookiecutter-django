from fabric.api import env, run, local


def live():
    """Connects to the server."""
    env.hosts = ['bankenverband.de']
    env.user = 'freshmilk'
    env.cwd = '/var/www/{{cookiecutter.project_name}}'
    env.connect_to = '{0}@{1}:{2}'.format(env.user, env.hosts[0], env.cwd)

def beta():
    """Connects to beta/testing server"""
    env.hosts = ['beta.{{cookiecutter.domain_name}}']
    env.user = 'username'
    env.cwd = '/var/www/beta.{{cookiecutter.project_name}}'
    env.connect_to = '{0}@{1}:{2}'.format(env.user, env.hosts[0], env.cwd)

def gitpull(tag=None):
    """Pulls upstream brunch on the server."""
    if tag is not None:
        run('git pull')
        run('git checkout %s' % tag)
    else:
        run('git pull')


def collectstatic():
    """Collect static files --noinput on server."""
    run('{{cookiecutter.repo_name}}/manage.py collectstatic --noinput')


def migrate():
    """Sync project database on server."""
    run('{{cookiecutter.repo_name}}/manage.py migrate')

def touch():
    """Touch the wsgi file."""
    run('touch {{cookiecutter.repo_name}}/{{cookiecutter.repo_name}}.wsgi')


def update(tag=None):
    """Runs gitpull, develop, collectstatic, migrate and touch.
    """
    gitpull(tag=tag)
    collectstatic()
    migrate()
    touch()


def dump():
    run('{{cookiecutter.repo_name}}/manage.py sqldump')


def sync_media():
    local('rsync -avzh --exclude "CACHE" -e ssh %s/../media/* ../media' % env.connect_to)


def sync_dump():
    local('rsync -avPhzL -e ssh %s/var/dump.sql.gz var' % env.connect_to)


def mirror():
    """Runs dump, sync_media, sync_dump and sqlimport."""
    dump()
    sync_media()
    sync_dump()
    local('{{cookiecutter.repo_name}}/manage.py sqlimport')