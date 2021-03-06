"""Setuptools setup script."""
from setuptools import setup

setup(name='DSH',
      version='0.4',
      description='Analyze DSH videos',
      url='https://github.com/steaime/DSHpy',
      author='Stefano Aime, Matteo Sabato',
      author_email='aime@seas.harvard.edu',
      license='GNU GPL',
      packages=['DSH'],
      install_requires=[
            'numpy',
            'scipy',
            'configparser',
            'emcee',
            'pandas'
      ],
      #test_suite='nose.collector',
      #tests_require=['nose'],
      zip_safe=False)