#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

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
    ],
    description="Allow calling registered custom functions (system tools, script functions, etc.)  via admin UI or manage.py command.",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='adminutilities',
    name='adminutilities',
    packages=find_packages(include=['adminutilities', 'adminutilities.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/Skylor-Tang/adminutilities',
    version='0.1.0',
    zip_safe=False,
)
