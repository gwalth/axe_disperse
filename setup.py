from setuptools import setup, find_packages

setup(
    name='axe_disperse',
    packages=find_packages(include=['axe_disperse', 'axe_disperse.*']),
    install_requires=['matplotlib',
                      'numpy',                     
                      ],

)

