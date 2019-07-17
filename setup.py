from pip._internal.req import parse_requirements
from setuptools import setup, find_packages

raw_requirements = parse_requirements('requirements/production.txt', session=False)
requirements = [str(ir.req) for ir in raw_requirements]

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='python-chain',
    version='1.0.2',
    scripts=['bin/build_chain.py'] ,
    author="QuintoAndar",
    author_email="daniel.fonseca@quintoandar.com.br",
    description="An easy to use pattern of function chaining on Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/quintoandar/python-chain/",
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
