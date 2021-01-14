from typing import ClassVar

import ulid
from django.urls import register_converter


class ULIDPathConverter:
    regex: ClassVar[str] = r"[0-9A-TV-Za-tv-z]{26}"

    def to_python(self, value: str) -> ulid.ULID:
        return ulid.from_str(value)

    def to_url(self, value: ulid.ULID) -> str:
        return str(value)


register_converter(ULIDPathConverter, "ulid")
