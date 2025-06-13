from setuptools import setup, find_packages

VERSION = '1.0.0'

setup_info = dict(
    name='Cryptool',
    version=VERSION,
    author='Jonas Ruppert',
    url='https://github.com/JonasRu07/cryptool_school.git',
    description='A tool for en/decryption from my school',
    packages=find_packages(exclude=('test',)),
    install_requires=[]
    )

setup(**setup_info)