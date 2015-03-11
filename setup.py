#!/usr/bin/env python

from setuptools import setup, os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name='PyBabel-json',
    version='0.2.0',
    description='PyBabel json gettext strings extractor',
    author='Anton Bykov aka Tigra San',
    author_email='tigrawap@gmail.com',
    long_description=read('README.rst'),
    packages=['pybabel_json'],
    url="https://github.com/tigrawap/pybabel-json",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    install_requires=[
        'babel',
    ],
    include_package_data=True,
    entry_points = """
        [babel.extractors]
        json = pybabel_json.extractor:extract_json
        """,
)
