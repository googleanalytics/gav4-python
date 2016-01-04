#!/usr/bin/env python

import os

from setuptools import find_packages
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))


with open(os.path.join(here, 'README.md')) as f:
  README = f.read()


REQUIREMENTS = [
    'google-api-python-client >= 1.2.0',
    'google-apputils >= 0.4.0',
]


setup(
    name='gav4',
    version='0.1.0',
    description='Google Analytics V4 API Compatibility Library',
    author='Google Analytics Platform',
    author_email='mcohoon+gav4-python@google.com',
    long_description=README,
    scripts=[],
    url='https://github.com/googleanalytics/gav4-python',
    packages=find_packages(),
    license='Apache 2.0',
    platforms='Posix; MacOS X; Windows',
    test_suite='nose.collector',
    tests_require=['nose', 'nose-cover3'],
    include_package_data=True,
    zip_safe=False,
    install_requires=REQUIREMENTS,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Internet',
    ]
)
