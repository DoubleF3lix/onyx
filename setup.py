import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="onyx-mclib",
    version="1.1.0",
    description="A python library to create minecraft datapacks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DoubleFelix/onyx/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
