from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.0.1",
    packages=find_packages(
        # All keyword arguments below are optional:
        where="src",  # '.' by default
        include=["mypackage*"],  # ['*'] by default
        exclude=["mypackage.tests"],  # empty by default
    ),
    install_requires=[
        "pandas",
        "matplotlib",
        "numpy",
        "scikit-learn",
        "black",
        "flake8",
        "isort",
    ],
)
