from setuptools import setup, find_packages

setup(
    name='textcleaner',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'spacy',
        'autocorrect',
        'contractions'
    ],
    author = "Dr. Partha Majumdar",
    author_email = "partha.majumdar@hotmail.com",
    description = "A simple text preprocessing package for NLP tasks",
)