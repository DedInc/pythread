from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="pythread",
    version="1.1.1",
    author="Maehdakvan",
    author_email="visitanimation@google.com",
    description="Useful module for comfortable managing with threading.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DedInc/pythread",
    project_urls={
        "Bug Tracker": "https://github.com/DedInc/pythread/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    python_requires='>=3.0'
)