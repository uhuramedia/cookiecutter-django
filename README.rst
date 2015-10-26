cookiecutter-django
===================

A cookiecutter_ template for Django 1.7 with Fabric, Bootstrap 3 etc.

.. _cookiecutter: https://github.com/audreyr/cookiecutter

* For Django 1.7
* Twitter Bootstrap 3

A reasoning behind why this is good layout, please read this article from RevSys http://bit.ly/1u299Uf


Usage
------

For installation and usage, follow these steps ::

    $ pip install cookiecutter

    $ cookiecutter https://github.com/uhuramedia/cookiecutter-django.git

    $ cd projectname/ && virtualenv env && source env/bin/activate

    $ pip install -r requirements/local.txt

    $ python manage.py runserver


.. image:: https://requires.io/github/uhuramedia/cookiecutter-django/requirements.svg?branch=master
     :target: https://requires.io/github/uhuramedia/cookiecutter-django/requirements/?branch=master
     :alt: Requirements Status


Notes
-----

As rule of thumb, use MySQL/MariaDB for smaller projects. Since using and setting up MariaDB is easy, this cookiecutter is configured to use it by default.
Use PostgreSQL for medium/big size projects as there is high changes we might need Postgres specific features like JSON, HStore etc. and obvious realibility.