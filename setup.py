#!/usr/bin/env python

from setuptools import setup, os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyBabel-json',
    version='0.1.0',
    description='PyBabel json gettext strings extractor',
    author='Anton Bykov aka Tigra San',
    author_email='tigrawap@gmail.com',
    long_description=read('README.rst'),
    packages=['pybabel_json'],
    url="https://github.com/tigrawap/pybabel-json",
    install_requires=[
        'babel',
    ],
    include_package_data=True,
    entry_points = """
        [babel.extractors]
        json = pybabel_json.extractor:extract_json
        """,
)
