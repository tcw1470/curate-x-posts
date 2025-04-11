import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="ScrapeX",
    version="0.0.1",
    author="Vcol Liym",
    author_email="vcolliym@gmail.com",
    description="Package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tcw1470/ScrapeX",
    packages=setuptools.find_packages(),
    entry_points={
        'console_scripts': [
            'scrapex = scrapex.__main__:main'
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
