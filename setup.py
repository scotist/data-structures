from setuptools import setup

setup(
    name='data_structures',
    description='Implementation of various data structures in python',
    version=0.1,
    author='AJ Wohlfert and Michael Sullivan',
    license='MIT',
    py_modules=['linked_list', 'doubly_linked', 'stack'],
    package_dir={'': 'src'},
    install_requires=[''],
    extras_require={'test': ['pytest', 'pytest-xdist', 'tox']},
)
