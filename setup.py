import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="mokarakaya-machine-learning-and-python-notes",
    version="0.0.3",
    author="mokarakaya",
    author_email="mokarakaya@gmail.com",
    description="Python notes with examples",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mokarakaya/machine-learning-and-python-notes",
    packages=setuptools.find_packages(),
    install_requires=required,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)