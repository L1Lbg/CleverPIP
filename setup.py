# setup.py

from setuptools import setup, find_packages

setup(
    name='SmartPIP',  # The name of your package
    version='0.1',
    packages=find_packages(),  # Automatically find all packages
    install_requires=['packaging'],  # List any dependencies you need here
    entry_points={
        'console_scripts': [
            'your-package = your_package.main:main',  # Define the entry point
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  # Specify the Python version required
)
