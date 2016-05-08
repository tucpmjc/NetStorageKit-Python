#!/usr/bin/env python

from distutils.core import setup


with open('README.rst', 'r') as f:
    readme = f.read()

setup (
    name = 'netstorageapi',
    version = '1.0.6',
    description = 'Akamai Netstorage API for Python',
    long_description = readme,
    packages = ['netstorageapi'],
    package_dir = {'netstorageapi': 'netstorageapi'},
    author = 'Astin Choi',
    author_email = 'asciineo@gmail.com',
    url = 'https://github.com/AstinCHOI/akamai-netstorage',
    classifiers=(
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ),
)