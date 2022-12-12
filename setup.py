from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='synthea_query',
    version="0.1.0",
    packages=find_packages(),
    url='https://github.com/wanghewen/synthea_query',
    author='hewen',
    description='A basic python package to query a synthetic EHR dataset',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=["pandas", "sqlalchemy", "psycopg2"]
)
