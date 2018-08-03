from setuptools import setup, Extension, find_packages
from Cython.Build import cythonize
import numpy


setup(name='mdr',
      version='0.0.1',
      description="python library to detect and extract listing data from HTML page",
      long_description="",
      author="Terry Peng",
      author_email="pengtaoo@gmail.com",
      url='https://github.com/tpeng/mdr',
      license='MIT',
      packages=find_packages(exclude=['tests', 'tests.*']),
      ext_modules = cythonize('mdr/_tree.pyx'),
      include_dirs = [numpy.get_include()],
      install_requires=['lxml', 'numpy', 'scipy', 'Cython'],
      zip_safe=False,
)
