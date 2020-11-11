from setuptools import setup, find_packages
from pypandoc import convert_file


def convert_markdown_to_rst(file):
    return convert_file(file, "rst")


setup(
    name="gregquests",
    version=open("version").read(),
    description="Wrapper around the requests library with extra features"
    " for cleaner, more resilient and possibly faster code",
    long_description=convert_markdown_to_rst("README.md"),
    url="https://github.com/gdubicki/gregquests",
    author="Greg Dubicki and the upstream projects authors",
    keywords=["requests", "timeout", "retry", "exception", "brotli"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
    ],
    packages=find_packages(),
    install_requires=[
        "requests<3",
        "urllib3>=1.25.1",
        "brotli",
    ],
    setup_requires=[
        "pypandoc",
    ],
)
