#!/usr/bin/env python


import sys
import os
from setuptools import setup, find_packages, Extension

description_txt = file('README.txt').read()

version = '0.0.1'

setup(name="mr.mount",
      version = version,
      packages=('mr', 'mr.mount'),
      maintainer= "Andreas Jung.",
      maintainer_email = "info@zopyx.com",
      author = "Andreas Jung, ZOPYX",
      author_email = "info@zopyx.com",
      description = 'Mount support for arbitrary filesystems within Plone',
      long_description = description_txt,
      url = "http://sf.net/projects/textindexng/",
      include_package_data=True,
      install_requires=('fs',
                        ),
      namespace_packages=('mr', 'mrmount'),
      extras_require=dict(
      ),
    )
