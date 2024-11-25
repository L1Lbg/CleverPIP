from setuptools import setup, find_packages

setup(
    name='SmartPIP',  # Your package name
    version='0.1.0',  # Initial version
    packages=find_packages(),  # Automatically find packages
    install_requires=[],  # Add dependencies here
    entry_points={
        'console_scripts': [
            'smartpip=src.main:cli',  # 'my_tool' is the CLI command
        ],
    },
    author='Luca',
    author_email='luca.baeyens@icloud.com',
    description='A simple PIP tool to automatically upgrade packages to your liking.',
    url='https://github.com/L1Lbg/SmartPIP',  # Your project URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
