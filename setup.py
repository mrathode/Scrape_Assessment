try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Link scraper',
    'version': '0.0.1',
    'install_requires': ['requests'],
    'packages': [],
    'scripts': [],
    'name': 'ScrapeIt'
}

setup(**config)
