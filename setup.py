import sys
import numpy

if sys.version_info[0] < 3:
    sys.exit('Sorry, Python < 3.x is not supported')

# Try using setuptools first, if it's installed
from setuptools import setup, find_packages


# Need to add all dependencies to setup as we go!
setup(name='pyway',
      packages=find_packages(),
      version='0.1',
      description="Python module for running Conway's Game of Life",
      author='Lucas C. Wheeler',
      author_email='lwheeler9@gmail.com',
      zip_safe=False,
      install_requires=["matplotlib","scipy","numpy","numba"],
      package_data={"":["*.h","src/*.h"]},
      classifiers=['Programming Language :: Python'])
