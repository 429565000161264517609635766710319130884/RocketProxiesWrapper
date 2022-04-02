import os
from setuptools import find_packages, setup

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='RocketProxies',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    description='Shitty wrapper for the RocketProxies API',
    keywords='wrapper api proxy',
    url='https://github.com/Mewzax/RocketProxiesWrapper',
    author='Mewzax',
    author_email='mewdev@pm.me',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ]
)