#!/usr/bin/env python

# Read https://github.com/django-extensions/django-extensions/issues/92
# Read: http://setuptools.readthedocs.io/en/latest/setuptools.html
# Look for find_packages, packages, package_dir
from setuptools import setup, find_packages

import cryptux

with open('README.md') as fd:
    setup(
        name='cryptux',
        version=cryptux.__version__,
        description='Simple wallet for Cryptocurrencies',
        long_description=fd.read(),
        author='Viet Le',
        author_email='vietlq85@gmail.com',
        url='https://github.com/VISCHub/cryptux',
        install_requires=['ecdsa>=0.13'],
        packages=['cryptux'],
        scripts=['tools/cryptux'],
        keywords=['crypto hdw wallet bitcoin ether'],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Topic :: Software Development :: Quality Assurance',
        ])
