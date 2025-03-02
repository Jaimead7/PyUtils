from os import path
from pathlib import Path

import tomli
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    longDescription: str = f.read()

configFilePath: str = path.join(Path(__file__).parent, 'dist', 'config', 'config.toml')
try:
    with open(configFilePath, 'rb') as f:
        myPyUtilsConfig: dict = tomli.load(f)
except tomli.TOMLDecodeError:
    raise tomli.TOMLDecodeError(f'Error with config file')

with open('requirements.txt') as f:
    requires: list = [line.replace('\n', '')
                      for line in f.readlines()
                      if line != '\n']

setup(
    name= myPyUtilsConfig['app']['name'],
    version= myPyUtilsConfig['app']['version'],
    description= 'Different utilities for general purpose usage on python projects.',
    long_description= longDescription,
    long_description_content_type= 'text/markdown',
    author= 'Jaimead7',
    author_email= 'alvarez.dia.jaime1@gmail.com',
    url= 'https://github.com/Jaimead7/MyPyUtils',
    packages= find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    license= 'MIT',
    install_requires= requires,
    extras_require= {
        'dev': [
            'pytest',
            'wheel'
        ],
    },
    python_requires= '>=3.10',
)
