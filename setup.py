#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'requests>=2.18.1'
]


def get_version():
    init = open(os.path.join(ROOT, 'stashy', '__init__.py')).read()
    return VERSION_RE.search(init).group(1)


setup(
    name='stashy',
    version=get_version(),
    description='The Stashy SDK for Python',
    long_description=open('README.rst').read(),
    author='Stashy.io',
    url='https://github.com/snclucas/stashy_python',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={
        'boto3': [
            'data/aws/resources/*.json',
            'examples/*.rst'
        ]
    },
    include_package_data=True,
    install_requires=requires,
    license="MIT",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
