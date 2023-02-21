#py setup.py sdist bdist_wheel
#py -m build
#py -m twine upload --verbose --repository testpypi dist/*
#py -m twine upload dist/*

from setuptools import setup, find_packages


setup(
    packages = find_packages(exclude=('tests','docs'))
)