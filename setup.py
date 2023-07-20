from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '1.0.0'
DESCRIPTION = 'Melt eases the process of experimenting, building, managing AI/ML/Dl development.'
LONG_DESCRIPTION = 'A lightweight package that allows to build and maintain AI/ML/DL projects.'

# Setting up
setup(
    name="melt",
    version=VERSION,
    author="SK HAPIJUL HOSSEN",
    author_email="<skhapijulhossen@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'ai', 'ml',
              'dl', 'machine learning', 'deep learning', 'development', 'mlops'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: AI/ML/DL Engineers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
