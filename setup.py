"""
ginit - GitHub Repository Initialization CLI
A simple command-line tool to automate git init, commit, and push to GitHub.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ginit-cli",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="CLI tool to automate GitHub repository initialization and pushing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ginit",
    py_modules=[
        "main",
        "config",
        "git_operations",
        "github_api",
        "licenses",
        "ginit"
    ],
    install_requires=[
        "PyGithub>=2.1.1",
        "python-dotenv>=1.0.0",
    ],
    entry_points={
        "console_scripts": [
            "ginit=ginit:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Version Control :: Git",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
)
