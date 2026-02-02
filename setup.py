"""
Missing module docstring ☝️🤓
"""
from setuptools import setup, find_packages

setup(
    name="meth",
    version="0.01",
    packages=find_packages(),
    install_requires=[],
    author="SellingJaguar",
    author_email="imagine@having.one",
    description="The best meth package ever.",
    long_description=open("DESCRIPTION.txt", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sellingjaguar/meth",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: Imagine having one",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)