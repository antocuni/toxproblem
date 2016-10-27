import sys
import os
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize('foo.py')

if 'USE_CYTHON' not in os.environ:
    ext_modules = []

# I would like to use a command line option instead of the USE_CYTHON env
# variable, but I don't know how to tell tox to pass it
## try:
##     sys.argv.remove("--no-compile")
## except ValueError:
##     pass
## else:
##     ext_modules = []


setup(name="toxproblem",
      ext_modules=ext_modules)
