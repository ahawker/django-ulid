from functools import partial
from typing import Optional

import pytest
import ulid
from django.urls import ResolverMatch, path

from django_ulid import path_converter


@pytest.fixture
def pattern():
    def view(request, id: ulid.ULID):
        assert isinstance(id, ulid.ULID)
        return id

    return partial(path, "<ulid:id>/", view)


def test_registered_converter(pattern):
    """Attempt to create a URLPattern object with 'ulid' registered converter. It will
    raise ImproperlyConfigured if it fails, otherwise it'll be created successfully."""
    pattern()


def test_resolving_pattern(pattern):
    """Attempt to resolve the URLPattern object with a path. A path with a valid ULID
    will return a ResolverMatch, with a ULID in the kwargs."""
    ptrn = pattern()
    test_ulid = "01EVZTQY9ZW1EG0QHBNRSQHN8S"
    match: Optional[ResolverMatch] = ptrn.resolve(f"{test_ulid}/")
    assert match
    assert match.kwargs["id"] == ulid.from_str(test_ulid)


def test_resolving_pattern_miss(pattern):
    """Attempt to resolve the URLPattern object with a path. A path without a valid ULID
    will return None."""
    ptrn = pattern()
    match = ptrn.resolve("not-a-ulid/")
    assert match is None
