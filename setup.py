from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="hUMAP",
    version="0.2",
    description="UMAP visualization for microbiota compositions with taxonomic structure.",
    url="http://github.com/granhussey/humap",
    author="Grant Hussey",
    license="MIT License",
    packages=["humap"],
    install_requires=[
        "matplotlib",
        "pandas",
        "seaborn",
        "numpy",
        "scipy",
        "numba",
        "umap-learn",
    ],
    scripts=["run_humap.py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    zip_safe=False,
)
