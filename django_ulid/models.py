import uuid
import ulid

from django.core import exceptions
from django.db import models
from django.db.migrations.serializer import BaseSerializer
from django.db.migrations.writer import MigrationWriter
from django.utils.translation import gettext as _


class ULIDSerializer(BaseSerializer):
    def serialize(self):
        return "ulid.ULID(%s)" % bytes(self.value), {"import ulid"}


MigrationWriter.register_serializer(ulid.ULID, ULIDSerializer)


def default_ulid():
    return ulid.ULID()


class ULIDField(models.UUIDField):
    """
    Django model field type for handling ULID's.

    This field type is natively stored in the DB as a UUID (when supported) and a string/varchar otherwise.
    """

    default_error_messages = {
        "invalid": _("“%(value)s” is not a valid ULID."),
    }
    description = "Universally Unique Lexicographically Sortable Identifier"
    empty_strings_allowed = False

    def __init__(self, verbose_name=None, **kwargs):
        super().__init__(verbose_name, **kwargs)
        self.max_length = 26
        self.serialize = True

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is None:
            return None
        if not isinstance(value, ulid.ULID):
            value = self.to_python(value)
        return value.to_uuid4() if connection.features.has_native_uuid_field else value.hex

    def get_internal_type(self):
        return "UUIDField"

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def to_python(self, value):
        if value is not None and not isinstance(value, ulid.ULID):
            try:
                if isinstance(value, uuid.UUID):
                    value = ulid.ULID.from_uuid(value)
                if isinstance(value, str):
                    value = ulid.ULID.from_str(value)
            except (AttributeError, ValueError):
                raise exceptions.ValidationError(
                    _("'%(value)s' is not a valid ULID."), code="invalid", params={"value": value}
                )
        return value

    def formfield(self, **kwargs):
        return super().formfield(**{
            'form_class': forms.ULIDField,
            **kwargs,
        })
