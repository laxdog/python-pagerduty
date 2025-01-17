#!/usr/bin/env python

from setuptools import setup, find_packages

import os
exec(compile(open(os.path.join('pagerduty', 'version.py')).read(), os.path.join('pagerduty', 'version.py'), 'exec'))

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

setup(
    name = 'python3-pagerduty',
    version = VERSION,
    description = 'Library for the PagerDuty service API',
    long_description = long_description,
    author = 'Samuel Stauffer',
    author_email = 'samuel@playhaven.com',
    url = 'http://github.com/prosperworks/python-pagerduty',
    packages = find_packages(),
    license = "BSD",
    entry_points = {
        "console_scripts": [
            "pagerduty = pagerduty.command:main",
        ],
    },
    classifiers = [
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
