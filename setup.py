from os import path
from pathlib import Path

import tomli
from setuptools import find_packages, setup

with open("README.md", "r") as f:
    longDescription: str = f.read()

configFilePath: str = path.join(Path(__file__).parent, 'dist', 'config', 'config.toml')
try:
    with open(configFilePath, 'rb') as f:
        myUtilsConfig: dict = tomli.load(f)
except tomli.TOMLDecodeError:
    raise tomli.TOMLDecodeError(f'Error with config file')

setup(
    name= myUtilsConfig['app']['name'],
    version= myUtilsConfig['app']['version'],
    description= 'Different utilities for general purpose usage on python projects.',
    package_dir={'': 'app'},
    packages= find_packages(where= 'app'),
    long_description= longDescription,
    long_description_content_type= 'text/markdown',
    url= 'https://github.com/Jaimead7/MyUtils',
    author= 'Jaimead7',
    author_email= 'alvarez.dia.jaime1@gmail.com',
    license= 'MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
    install_requires= ['tomli >= 2.2.1',],
    extra_require= {
        'dev': [
            'pytest',
        ],
    },
    python_requires= '>=3.10',
)
