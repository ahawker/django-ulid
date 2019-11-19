"""
    django_ulid
    ~~~~~~~~~~~

    Universally Unique Lexicographically Sortable Identifier (ULID) support in Django.

    :copyright: (c) 2019 Andrew Hawker.
    :license: Apache 2.0, see LICENSE for more details.
"""
import ast
import re


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


version_regex = re.compile(r'__version__\s+=\s+(.*)')


def get_version():
    with open('django_ulid/__init__.py', 'r') as f:
        return str(ast.literal_eval(version_regex.search(f.read()).group(1)))


def get_long_description():
    with open('README.rst') as f:
        return f.read()


setup(
    name='django-ulid',
    version=get_version(),
    author='Andrew Hawker',
    author_email='andrew.r.hawker@gmail.com',
    url='https://github.com/ahawker/django-ulid',
    license='Apache 2.0',
    description='Universally Unique Lexicographically Sortable Identifier (ULID) support in Django',
    long_description=get_long_description(),
    packages=['django_ulid'],
    python_requires='>=3.5',
    install_requires=['Django>=2.1', 'ulid-py>=0.0.9'],
    classifiers=(
        'Development Status :: 4 - Beta',
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 2.1",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules'
    )
)
