#py setup.py sdist bdist_wheel

from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.1.8'
DESCRIPTION = 'Japanese Chatbot'

with open('./LICENSE.md', 'r') as license_md:
    license_file = license_md.read()
    

with open('./README.md', 'r') as readme:
    LONG_DESCRIPTION = readme.read()

# Setting up
with open('./requirements.txt','r') as requirements_text:
    required = requirements_text.read().split("\n")

setup(
    name="nagonbot",
    version=VERSION,
    author="Gabriel Fioravante Di Sciascio (FDSGAB)",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    url='https://github.com/FDSGAB/nagonbot',
    license = license_file,
    packages = find_packages(exclude=('tests','docs')),
    install_requires = required,
    keywords=['python', 'chatbot', 'japanese', 'nagon', 'bot'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)