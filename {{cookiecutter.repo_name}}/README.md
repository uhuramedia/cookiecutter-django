{{cookiecutter.project_name}}
============================

{{cookiecutter.description}}


Install
-------

For installation and usage, follow these steps


    $ cd projectname
    $ virtualenv env && source env/bin/activate

    $ pip install -r requirements/local.txt

    $ python manage.py migrate

    $ python manage.py runserver


Deploy
------

Basic fabric commands are included for deployment

    $ fab live update

Sync with live version of media files and database

    $ fab live mirror
