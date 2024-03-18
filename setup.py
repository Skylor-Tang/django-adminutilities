#!/usr/bin/env python

"""The setup script."""
import re
import subprocess
from setuptools import setup, find_packages


# Get the latest release version from git tags
latest_release = subprocess.check_output(['git', 'describe', '--tags']).decode().strip()
latest_version = re.match(r'^.*?(\d+\.\d+\.\d+).*$', latest_release).group(1)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = [ ]

setup(
    author="tangmeijian",
    author_email='tang1996mei@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    description="Allow calling registered custom functions (system tools, script functions, etc.)  via admin UI or manage.py command.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['django', 'utilities', 'admin'],
    name='django-adminutilities',
    packages=find_packages(include=['adminutilities', 'adminutilities.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Skylor-Tang/django-adminutilities',
    version=latest_version,
    zip_safe=False,
)
