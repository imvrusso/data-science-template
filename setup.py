import os
from setuptools import find_packages, setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='src',
    description='Project description',
    long_description=read('README.md'),
    author='Valerio Russo',
    packages=find_packages(),
)
