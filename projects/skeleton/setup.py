###Setup python script to test for project directory structure

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    
    'name':'Project name',
    'description': 'New Project',
    'version': '0.1',
    'author': 'Alhamdu U Bello',
    'author_email': 'alhamdubello@gmail.com',
    'url':'http://url',
    'download_url': 'http://github.com/download/code',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts': []
}

setup(**config)