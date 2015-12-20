contact
*******

Django application

Install
=======

Virtual Environment
-------------------

::

  virtualenv --python=python3.4 venv-contact
  source venv-contact/bin/activate
  pip install --upgrade pip

  pip install -r requirements/local.txt

Testing
=======

::

  find . -name '*.pyc' -delete
  py.test -x

Usage
=====

::

  py.test -x && \
      touch temp.db && rm temp.db && \
      django-admin.py syncdb --noinput && django-admin.py migrate --all --noinput && \
      django-admin.py demo_data_login && \
      django-admin.py demo_data_contact && \
      django-admin.py runserver

Release
=======

https://www.pkimber.net/open/
