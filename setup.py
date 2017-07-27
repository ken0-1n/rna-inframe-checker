#!/usr/bin/env python

from distutils.core import setup

setup(
    name='rna-inframe-checker',
    version='0.0.1',
    author_email='kchiba@hgc.jp',
    package_dir = {'': 'lib'},
    packages=['inframe_checker'],
    scripts=['inframe_checker'],
    license='GPL-3'
)

