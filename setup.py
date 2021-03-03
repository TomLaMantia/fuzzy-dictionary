import os
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

this_directory = os.path.abspath(os.path.dirname(__file__))

# read the contents of requirements.txt
with open(os.path.join(this_directory, 'requirements.txt'),
          encoding='utf-8') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="fuzzy-dictionary",
    version="0.1",
    author="Tom LaMantia",
    author_email="tom.lamanti@mail.utoronto.ca",
    description="A dictionary-like object that supports fuzzy key lookup.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
