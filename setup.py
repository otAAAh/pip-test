"""Number Package Setup"""

import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


setuptools.setup(
    name='number',
    version='0.2',
    scripts=['number.py'],
    author="otAAAh",
    author_email="benjamin@knapp-programmieurng.de",
    description="Number test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/otAAAh/pip-test",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
