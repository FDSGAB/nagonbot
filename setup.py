#py setup.py sdist bdist_wheel
#py -m build
#py -m twine upload --verbose --repository testpypi dist/*
#py -m twine upload dist/*

from setuptools import setup


setup()