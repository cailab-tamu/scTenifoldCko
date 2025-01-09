from setuptools import setup, find_packages

setup(
    name="scTenifoldCko",
    version="0.1.0",
    description="A single-cell data analysis tool for simulating cell-cell communication knockout (CKO) and analyzing gene expression changes.",
    author="James Cai",
    author_email="jcai@tamu.edu",
    url="https://github.com/cailab-tamu/scTenifoldCko",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0",
        "scanpy>=1.9.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
