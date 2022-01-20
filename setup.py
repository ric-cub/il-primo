from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="il-primo",
    version="0.0.1",
    author="Ricardo Cubillos",
    author_email="rcg@g.vvv",
    description="A test description",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/il-primo/homepage/",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
    ],
)