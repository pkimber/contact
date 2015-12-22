contact
*******

Django application

To Do
=====

- I think I should remove the ``hourly_rate`` field from the ``Contact`` model.
  It probably belongs in the ``crm`` or ``invoice`` app.
- Do we want a ``slug`` field in the ``Contact`` model.  I think we probably
  do.
- Need to think about how to link users to the contact model.  The contact
  *is a* user.  The ``UserContact`` field links one or more users to a contact.
  Need to write some tests for this.  The original system only allowed a user
  to be linked to one contact.  I think this should be changed to allow a user
  to be linked to any number of contacts.
- The migration is currently losing the ``industry`` field.  See
  ``0006_auto_20151220_2207.py`` for the commented out field.

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
