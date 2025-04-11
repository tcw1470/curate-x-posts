import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="twiX",
    version="0.0.1",
    author="TCW",
    author_email="1470pancake@gmail.com",
    description="Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tcw1470/twix",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'twix = twix.__main__:main'
        ]
    },
    install_requires=[
        'twikit',
        'dotenv',
        'asyncio',
        'argparse',
        'pandas',
        'tqdm',
        'datetime',
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.10',
)
