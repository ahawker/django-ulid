django-ulid
===========

|Build Status| |codecov| |Code Climate| |Issue Count|

|PyPI Version| |PyPI Versions|

`Universally Unique Lexicographically Sortable Identifier
(ULID) <https://github.com/alizain/ulid>`__ support in
`Django <https://www.djangoproject.com/>`__.

Status
~~~~~~

This project is actively maintained.

Installation
~~~~~~~~~~~~

To install django-ulid from `pip <https://pypi.python.org/pypi/pip>`__:

.. code:: bash

       $ pip install django-ulid

To install ulid from source:

.. code:: bash

       $ git clone git@github.com:ahawker/django-ulid.git
       $ cd django-ulid && python setup.py install

Usage
~~~~~

Adding a ULID field to your Django models is straightforward. It can be
a normal field or a primary key.

.. code:: python

   from django.db import models
   from django_ulid.models import default, ULIDField

   class Person(models.Model):
       id = ULIDField(default=default, primary_key=True, editable=False)

Passing in ``default`` to the ``ULIDField`` will automatically create a
default value using the
`ulid.new <https://ulid.readthedocs.io/en/latest/api.html#ulid.api.new>`__
function. If you do not want a default value, ``None`` by default, feel
free to omit it.

.. code:: python

   from django.db import models
   from django_ulid.models import ULIDField

   class Person(models.Model):
       optional_id = ULIDField()

Adding a ULID field to your `Django REST
Framework <https://www.django-rest-framework.org/>`__ serializers is
also straightforward.

Simply importing the ``django_ulid.serializers`` module will
automatically register the ``ULIDField`` serializer by overriding the
`serializer_field_mapping <https://www.django-rest-framework.org/api-guide/serializers/#customizing-field-mappings>`__
on the default
`ModelSerializer <https://www.django-rest-framework.org/api-guide/serializers/#modelserializer>`__.

.. code:: python

   from django_ulid import serializers

If you are using a ULID as a primary key on a model, you need to create
a custom
`PrimaryKeyRelatedField <https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield>`__
to automatically serialize the instance through the foreign key.

.. code:: python

   import functools
   from django_ulid.serializers import ULIDField
   from rest_framework import serializers

   PersonPrimaryKeyRelatedField = functools.partial(serializers.PrimaryKeyRelatedField,
                                                    allow_null=True,
                                                    allow_empty=True,
                                                    pk_field=ULIDField(),
                                                    queryset=Person.objects.all())

   class OrganizationSerializer(serializers.ModelSerializer):
       owner = PersonPrimaryKeyRelatedField()

Contributing
~~~~~~~~~~~~

If you would like to contribute, simply fork the repository, push your
changes and send a pull request. Pull requests will be brought into the
``master`` branch via a rebase and fast-forward merge with the goal of
having a linear branch history with no merge commits.

License
~~~~~~~

`Apache 2.0 <LICENSE>`__

Dependencies
~~~~~~~~~~~~

-  `Django <https://github.com/django/django>`__
-  `ulid-py <https://github.com/ahawker/ulid>`__

.. |Build Status| image:: https://travis-ci.org/ahawker/django-ulid.svg?branch=master
   :target: https://travis-ci.org/ahawker/django-ulid
.. |codecov| image:: https://codecov.io/gh/ahawker/django-ulid/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/ahawker/django-ulid
.. |Code Climate| image:: https://codeclimate.com/github/ahawker/django-ulid/badges/gpa.svg
   :target: https://codeclimate.com/github/ahawker/django-ulid
.. |Issue Count| image:: https://codeclimate.com/github/ahawker/django-ulid/badges/issue_count.svg
   :target: https://codeclimate.com/github/ahawker/django-ulid
.. |PyPI Version| image:: https://badge.fury.io/py/django-ulid.svg
   :target: https://badge.fury.io/py/django-ulid
.. |PyPI Versions| image:: https://img.shields.io/pypi/pyversions/django-ulid.svg
   :target: https://pypi.python.org/pypi/django-ulid
