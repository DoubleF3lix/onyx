import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="onyx-mclib",
    version="2.0.0",
    description="An API for minecraft data pack generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Double-Felix/Onyx/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
