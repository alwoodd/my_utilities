from setuptools import setup, find_packages

setup(
    name='my_utilities',               # Package name
    version='1.0.0',                    # Initial version
    author='Dan Alwood',
    author_email='dalwood@yahoo.com',
    description='Common utility functions for local projects',
    packages=find_packages(),           # Automatically find packages within the directory
    install_requires=[],                # Add any dependencies if necessary
)
