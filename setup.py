import os
from setuptools import find_packages, setup

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

version = os.getenv(
    "VERSION", "0.0.0"
)  # Fallback to '0.0.0'version = os.getenv('PACKAGE_VERSION', '0.0.0')  # Fallback to '0.0.0'



setup(
    name="CD",
    version=version,
    author="Marcin Duda",
    author_email="dudamarcin539@gmail.com",
    description="Students presence",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Equu1/CD",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": ["CD=src:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
)