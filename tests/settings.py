"""
    settings
    ~~~~~~~~

    Django settings for tests.
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3'
    }
}

SECRET_KEY = 'secretkey'

INSTALLED_APPS = [
    'django_ulid',
    'tests'
]
