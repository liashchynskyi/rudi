import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rudi',
    version='1.0',
    scripts=['bin/rudi'],
    author="Petro Liashchynskyi",
    description="Small, fast and simple Python CLI image converter for CNNs.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/liashchynskyi/rudi",
    packages=setuptools.find_packages(),
    install_requires=[
        'click',
        #'Augmentor',
        'Pillow'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
