from setuptools import setup, find_packages
setup(
    name="math_package",
    version="1.0.0",
    description="A simple math operations package",
        long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Ken",
    author_email="lukenin9@gmail.com",
    url="https://github.com/Zoeldyeck/Package-1",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)