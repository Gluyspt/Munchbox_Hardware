from setuptools import setup
from Cython.Build import cythonize
import os

files = [
    "main.py",
    "pipeline.py",
    "ocr.py",
    "cleanup.py",
    "config.py",
]

setup(
    name="MunchBox OCR Pipeline",
    ext_modules=cythonize(
        files,
        compiler_directives={
            "language_level": "3",
        },
    ),
)