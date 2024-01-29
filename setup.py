from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'Projeto final da disciplina de Programação Orientada a Objetos II'
LONG_DESCRIPTION = 'Este projeto tem como objetivo por em prática alguns dos conhecimentos adquiridos ao longo da disciplina.'

setup(
    name = 'searchft',
    version = VERSION,
    author = 'liedson',
    author_email = 'fabricoliedson@gamil.com',
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    packages = find_packages(),
    install_require = 'googlesearch',

    keywords = ['python', 'web', 'search'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
    ]
 
)