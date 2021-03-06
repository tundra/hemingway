#- Copyright 2013 GOTO 10.
#- Licensed under the Apache License, Version 2.0 (see LICENSE).

import setuptools

setuptools.setup(
  name = "Hemingway",
  version = "0.0.1",
  description = "",
  author = "GOTO 10",
  url = "http://goto-10.github.io/hemingway",
  packages = setuptools.find_packages(),
  entry_points = {
    'console_scripts': [
      'hemingway = hemingway.main:main',
    ]
  },
  install_requires = ['markdown', 'pygments', 'watchdog', 'glob2'],
  include_package_data = True
)
