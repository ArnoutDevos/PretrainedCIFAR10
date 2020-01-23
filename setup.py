from setuptools import setup, find_packages

with open("requirements.txt") as requirements_file:
    REQUIREMENTS = requirements_file.readlines()

setup(
    name="PretrainedCIFAR10",
    version="1.0.0",
    author='Arnout Devos',
    packages=find_packages(),
    entry_points = {
        'console_scripts': [
            'quantize=quantize:main',
        ]
    },
    install_requires=REQUIREMENTS,

)
