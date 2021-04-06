#!/usr/bin/env python

from setuptools import setup

from codecs import open
from os import path
from wagtail_editor_extensions import __version__


install_requires = [
    'wagtail>=2,<2.5'
]

documentation_extras = [
    'sphinxcontrib-spelling>=2.3.0',
    'Sphinx>=1.5.2',
    'sphinx-autobuild>=0.6.0',
    'karma_sphinx_theme>=0.0.6',
]

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='wagtail-editor-extensions',
    version=__version__,
    description='Wagtail text editor additions for DraftJS',
    long_description=long_description,
    author='Matthew Wimberly',
    author_email='matthew.wimb@gmail.com',
    url='https://github.com/mattdood/wagtail-editor-extensions/',
    download_url='https://pypi.python.org/pypi/wagtail-editor-extensions',
    license='MIT',
    packages=[
        'wagtail_editor_extensions'
    ],
    install_requires=install_requires,
    extras_require={
        'docs': documentation_extras
    },
    include_package_data=True,
    keywords=['wagtail', 'draftjs', 'django'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'Topic :: Internet :: WWW/HTTP :: Site Management',
    ],
)
