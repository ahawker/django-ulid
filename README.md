# django-ulid

[![Build Status](https://travis-ci.org/ahawker/django-ulid.svg?branch=master)](https://travis-ci.org/ahawker/django-ulid)
[![codecov](https://codecov.io/gh/ahawker/django-ulid/branch/master/graph/badge.svg)](https://codecov.io/gh/ahawker/django-ulid)
[![Code Climate](https://codeclimate.com/github/ahawker/django-ulid/badges/gpa.svg)](https://codeclimate.com/github/ahawker/django-ulid)
[![Issue Count](https://codeclimate.com/github/ahawker/django-ulid/badges/issue_count.svg)](https://codeclimate.com/github/ahawker/django-ulid)

[![PyPI Version](https://badge.fury.io/py/django-ulid.svg)](https://badge.fury.io/py/django-ulid)
[![PyPI Versions](https://img.shields.io/pypi/pyversions/django-ulid.svg)](https://pypi.python.org/pypi/django-ulid)

[Universally Unique Lexicographically Sortable Identifier (ULID)](https://github.com/alizain/ulid) support in [Django](https://www.djangoproject.com/).

### Status

This project is actively maintained.

### Installation

To install django-ulid from [pip](https://pypi.python.org/pypi/pip):
```bash
    $ pip install django-ulid
```

To install ulid from source:
```bash
    $ git clone git@github.com:ahawker/django-ulid.git
    $ cd django-ulid && python setup.py install
```

### Usage

Adding a ULID field to your Django models is straightforward. It can be a normal field or a primary key.

```python
from django.db import models
from django_ulid.models import default_ulid, ULIDField

class Person(models.Model):
    id = ULIDField(primary_key=True, default=default_ulid, editable=False)
```

Passing in `default` to the `ULIDField` will automatically create a default value using the [ulid.new](https://ulid.readthedocs.io/en/latest/api.html#ulid.api.new) function.
If you do not want a default value, `None` by default, feel free to omit it.

```python
from django.db import models
from django_ulid.models import ULIDField

class Person(models.Model):
    optional_id = ULIDField()
```

Adding a ULID field to your [Django REST Framework](https://www.django-rest-framework.org/) serializers is also straightforward.

Simply importing the `django_ulid.serializers` module will automatically register the `ULIDField` serializer by overriding
the [serializer_field_mapping](https://www.django-rest-framework.org/api-guide/serializers/#customizing-field-mappings) on the default [ModelSerializer](https://www.django-rest-framework.org/api-guide/serializers/#modelserializer).

```python
from django_ulid import serializers
```

If you are using a ULID as a primary key on a model, you need to create a custom [PrimaryKeyRelatedField](https://www.django-rest-framework.org/api-guide/relations/#primarykeyrelatedfield) to automatically serialize
the instance through the foreign key.

```python
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
```

### Contributing

If you would like to contribute, simply fork the repository, push your changes and send a pull request.
Pull requests will be brought into the `master` branch via a rebase and fast-forward merge with the goal of having a linear branch history with no merge commits.

### License

[Apache 2.0](LICENSE)

### Dependencies

* [Django](https://github.com/django/django)
* [ulid-py](https://github.com/ahawker/ulid)
