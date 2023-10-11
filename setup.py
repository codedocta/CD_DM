from setuptools import setup, find_packages
from Directory_Manager import version

setup(
    name='CD_MD',
    version= version.__version__,
    description='A package containing utilities for file and directory management, ZIP operations, and more.',
    author='Your Name',  # Replace with your name
    author_email='your.email@example.com',  # Replace with your email
    url='https://github.com/codedocta/CD_MD',  # Replace with your repository URL
    packages=find_packages(),
    install_requires=[
        'pyside6=6.5.3',  # For FileDialog with PySide6
        'pyqt6=6.5.2',  # For FileDialog with PyQt6
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Adjust if you're using a different license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
    ],
    keywords='file management, directory management, zip operations',
    project_urls={
        'Bug Reports': 'https://github.com/codedocta/CD_MD/issues',  # Replace with your issues URL
        'Source': 'https://github.com/codedocta/CD_MD/',  # Replace with your repository URL
    },
)
