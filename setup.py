#py setup.py sdist bdist_wheel
#py -m twine upload --repository testpypi dist/*

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.9'
DESCRIPTION = 'Japanese Chatbot'

with open('./LICENSE.md', encoding = 'utf8') as license_md:
    license_file = license_md.read()
    

with open('./README.md', encoding = 'utf8') as readme:
    LONG_DESCRIPTION = readme.read()

with open('./requirements.txt', encoding = 'utf8') as requirements_text:
    required = requirements_text.read().split("\n")

setup(
    name="nagonbot",
    version=VERSION,
    author="Gabriel Fioravante Di Sciascio (FDSGAB)",
    maintainer="Gabriel Fioravante Di Sciascio (FDSGAB)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/FDSGAB/nagonbot',
    license = license_file,
    packages = find_packages(exclude=('tests','docs')),
    install_requires = required,
    keywords=['python', 'chatbot', 'japanese', 'nagon', 'bot', 'artificial intelligence', 'virtual assistant'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        'Environment :: Console',
        "License :: OSI Approved :: MIT License",
        'Intended Audience :: End Users/Desktop',
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.7',
)