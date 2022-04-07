from setuptools import setup

setup(
    name = 'Sudoku solver',
    version = '0.1',
    author = 'Dawid Drążewski',
    license = 'MIT',
    package_dir = {'': 'src'},
    py_modules = ['controller', 'interface', 'model']
)