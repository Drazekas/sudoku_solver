from setuptools import setup

setup(
    name = 'Sudoku solver',
    version = '1.0',
    author = 'Dawid Drążewski',
    license = 'MIT',
    package_dir = {'': 'src'},
    py_modules = ['controller', 'interface', 'model'],
    install_requires=[]
)