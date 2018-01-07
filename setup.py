#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click==6.7',
    'urwid==1.3.1',
    'pydub==0.20.0',
    'python-vlc==3.0.101',
    # TODO: put package requirements here
]

setup_requirements = [
    'pytest-runner',
    # TODO(yeonghoey): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='ankia',
    version='0.1.0',
    description="Anki Automations",
    long_description=readme + '\n\n' + history,
    author="Yeongho Kim",
    author_email='yeonghoey@gmail.com',
    url='https://github.com/yeonghoey/ankia',
    packages=find_packages(include=['ankia']),
    entry_points={
        'console_scripts': [
            'ankia=ankia.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='ankia',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
