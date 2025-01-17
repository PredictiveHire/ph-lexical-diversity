#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()


requirements = ['scipy>=1.0.0', 'textblob>=0.15.3']

setup(
    author="Lucas Shen YS",
    author_email='shen1ys@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="A small module to compute textual lexical richness",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords=['lexical diversity', 'lexical richness', 'vocabulary diversity', 'lexical density', 'lexical'],
    name='lexical_diversity',
    packages=find_packages(include=['lexical_diversity']),
    url='https://github.com/PredictiveHire/ph-lexical-diversity',
    version='0.1.6'
)
