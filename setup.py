from setuptools import setup, find_packages

__version = "1.0.0"

setup(
    name="sardana_locum",
    version=__version,
    install_requires=["sardana", "setuptools"],
    description="Locum sardaba controller"
)
