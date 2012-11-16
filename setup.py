#!/usr/bin/env python

from setuptools import setup, find_packages
from brplatform import version

setup(
    name = "mongorocketsdk",
    packages = ['mongorocket',],
    version = version.VERSION,
    author = "Alan Illing",
    description = ("Software development kit for the Mongo Rocket platform"),
    license = "GPL",
    url = "https://github.com/ailling/mongorocketsdk",
    install_requires=['requests>=0.14.1',]
)
