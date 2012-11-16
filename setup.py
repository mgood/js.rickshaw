#!/usr/bin/python

import setuptools
from setuptools import find_packages

setuptools.setup(
  name = 'js.rickshaw',
  version = '1.1.2',
  license = 'BSD',
  description = 'Fanstatic package for Rickshaw',
  long_description = open('README.txt').read(),
  author = 'Matt Good',
  author_email = 'matt@matt-good.net',
  url = 'http://github.com/mgood/js.rickshaw/',
  platforms = 'any',
  packages=find_packages(),
  namespace_packages=['js'],
  include_package_data=True,
  zip_safe = False,
  install_requires=[
    'fanstatic',
    'js.d3',
  ],
  entry_points={
    'fanstatic.libraries': [
      'rickshaw = js.rickshaw:library',
    ],
  },
)
