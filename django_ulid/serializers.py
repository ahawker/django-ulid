"""
    django_ulid/serializers
    ~~~~~~~~~~~~~~~~~~~~~~~

    Contains functionality for Django REST Framework (DRF) serializer support.
"""
import ulid
from django.utils.translation import gettext as _
from rest_framework import fields, serializers

from . import models


class ULIDField(fields.Field):
    """
    Django REST Framework (DRF) serializer field type for handling ULID's.
    """
    default_error_messages = {
        'invalid': _('"{value}" is not a valid ULID.'),
    }

    def to_internal_value(self, data):
        try:
            return ulid.parse(data)
        except (AttributeError, ValueError):
            self.fail('invalid', value=data)

    def to_representation(self, value):
        return str(ulid.parse(value))


# Register the DRF serializer field with the Django ULID model field so the DRF model
# serializer can automatically detect/use the field without requiring serializers to specify it.
serializers.ModelSerializer.serializer_field_mapping[models.ULIDField] = ULIDField
