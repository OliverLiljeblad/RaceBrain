from setuptools import setup, find_packages

setup(
    name="racebrain",
    version="0.1.0",
    description="Machine learning predictions for Formula 1 races",
    author="Oliver (OByte-Tech)",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "numpy",
        "scikit-learn",
        "xgboost",
        "matplotlib",
        "seaborn",
        "requests",
    ],
)
