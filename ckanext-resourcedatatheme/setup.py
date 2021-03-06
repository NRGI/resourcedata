#!/usr/bin/env/python
from setuptools import setup

setup(
    name='ckanext-resourcedatatheme',
    version='0.1',
    description='',
    license='AGPL3',
    author='',
    author_email='',
    url='',
    namespace_packages=['ckanext'],
    packages=['ckanext.resourcedatatheme'],
    zip_safe=False,
    entry_points = """
        [ckan.plugins]
        resourcedata_theme = ckanext.resourcedatatheme.plugins:CustomTheme
    """
)
