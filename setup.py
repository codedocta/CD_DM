from setuptools import setup, find_packages
from Directory_Manager import version

setup(
    name='CD_MD',
    version=version.__version__,
    description='A package containing utilities for file and directory management, ZIP operations, and more.',
    author='Nicholas Capasso',
    author_email='codedocta@gmail.com',
    url='https://github.com/codedocta/CD_MD',
    packages=find_packages(),
    install_requires=[
        'pyside6==6.5.3',  # For FileDialog with PySide6
        'pyqt6==6.5.2',  # For FileDialog with PyQt6
    ],
    classifiers=[
        'Development Status :: 2 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # Adjust if you're using a different license

        'Programming Language :: Python :: 3.11',
    ],
    keywords='file management, directory management, zip operations',
    project_urls={
        'Bug Reports': 'https://github.com/codedocta/CD_MD/issues',  # Replace with your issues URL
        'Source': 'https://github.com/codedocta/CD_MD/',  # Replace with your repository URL
    },
)
