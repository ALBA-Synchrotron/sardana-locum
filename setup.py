from setuptools import setup, find_packages

__version = "1.1.2"

setup(
    name="sardana_locum",
    version=__version,
    packages=find_packages(),
    install_requires=["sardana", "setuptools"],
    description="Locum sardaba controller"
)
