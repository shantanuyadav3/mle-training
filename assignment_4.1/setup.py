from setuptools import setup, find_packages

setup(
    name="shantanuyadav",
    version="0.0.3",
    packages=find_packages(
        # All keyword arguments below are optional:
        where="src/.",  # '.' by default
        include=["*"],  # ['*'] by default
        exclude=["shantanuyadav.tests"],  # empty by default
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
