import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AutoTrader-Web-API-Stocks-Developer",
    version="1.3.5",
    author="Stocks Developer",
    author_email="help@stocksdeveloper.in",
    description="Broker-independent Python trading API for automated, single or multi-account trading across 40+ Indian brokers. Part of AutoTrader Web by Stocks Developer.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stocksdeveloper.in/",
    project_urls={
        "Homepage": "https://stocksdeveloper.in/",
        "Documentation": "https://stocksdeveloper.in/documentation/client-setup/python-library/",
        "Source": "https://github.com/stocks-developer/autotrader-python-lib",
    },
    packages=setuptools.find_packages(),
    install_requires=['requests'],    
    classifiers=[
        "Programming Language :: Python :: 3",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Intended Audience :: Information Technology",
        "Topic :: Office/Business :: Financial :: Investment"
    ],
    python_requires='>=3.6',
)