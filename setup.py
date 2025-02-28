from setuptools import find_packages, setup

with open("README.md", "r") as f:
    longDescription: str = f.read()

setup(
    name= 'myUtils',
    version= '0.0.1',
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
    install_requires= [],
    extra_require= {
        'dev': [
            'pytest',
        ],
    },
    python_requires= '>=3.10',
)