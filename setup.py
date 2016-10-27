import sys
from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = cythonize('foo.py')

try:
    sys.argv.remove("--no-compile")
except ValueError:
    pass
else:
    ext_modules = []


setup(name="toxproblem",
      ext_modules=ext_modules)
