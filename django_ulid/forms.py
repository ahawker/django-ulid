"""
    django_ulid/forms
    ~~~~~~~~~~~~~~~~~

    Contains functionality for Django form support.
"""
import ulid
from django import forms
from django.core import exceptions
from django.utils.translation import gettext as _


class ULIDField(forms.CharField):
    """
    Django form field type for handling ULID values.
    """
    def prepare_value(self, value):
        return str(ulid.parse(value))

    def to_python(self, value):
        value = super().to_python(value)

        if value in self.empty_values:
            return None
        try:
            return ulid.parse(value)
        except (AttributeError, ValueError):
            raise exceptions.ValidationError(_('Enter a valid ULID.'), code='invalid')
