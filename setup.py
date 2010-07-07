#!/usr/bin/env python

from setuptools import setup, find_packages
 
setup (
    name='bputils',
    version='0.1',
    description='Dependency free utilities',
    author='Ian Lewis',
    author_email='ianmlewis@beproud.jp',
    url='https://project.beproud.jp/hg/bputils/',
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Programming Language :: Python',
      'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    packages=find_packages("bputils"),
    test_suite="bputils.tests",
    zip_safe=True,
)
