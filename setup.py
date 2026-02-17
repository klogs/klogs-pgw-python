"""Setup script for Klogs Payment Gateway Python Client"""

from setuptools import setup, find_packages
import os


# Read README for long description
def read_file(filename):
    with open(os.path.join(os.path.dirname(__file__), filename), encoding='utf-8') as f:
        return f.read()


# Read requirements
def read_requirements():
    with open('requirements.txt') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]


setup(
    name='klogs-pgw',
    version='1.0.0',
    description='Klogs Payment Gateway Python client package',
    long_description=read_file('README.md'),
    long_description_content_type='text/markdown',
    author='Klogs',
    author_email='info@klogs.io',
    url='https://github.com/klogs-hub/paymentgateway-python',
    packages=find_packages(exclude=['tests', 'examples']),
    install_requires=read_requirements(),
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial',
    ],
    keywords='klogs payment gateway api client credit-card',
    project_urls={
        'Documentation': 'https://github.com/klogs-hub/paymentgateway-python',
        'Source': 'https://github.com/klogs-hub/paymentgateway-python',
        'Bug Reports': 'https://github.com/klogs-hub/paymentgateway-python/issues',
    },
)
