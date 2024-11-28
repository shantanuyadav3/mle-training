from setuptools import setup, find_packages

setup(
    name="shantanuyadav",
    version="0.0.3",
    packages=find_packages(where="src"),  # Specify the "src" directory
    package_dir={"": "src"},  # Map "src" as the root for packages
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
