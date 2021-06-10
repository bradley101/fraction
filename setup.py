import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Fraction", # Replace with your own username
    version="1.5.1",
    author="Shantanu Banerjee",
    author_email="hi@shantanubanerjee.com",
    description="Fraction carries out all the fraction operations including addition, subtraction, multiplication, division, reciprocation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bradley101/fraction",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)