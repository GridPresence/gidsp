import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="GiDsp",
    version="0.0.1",
    author="Jeremy Pavier",
    author_email="generiter@gmx.com",
    description="A package for floating point DSP operations on audio files.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GridPresence/GiDsp",
    license="MIT",
    packages=setuptools.find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points = {
        'console_scripts': []
    }
)
