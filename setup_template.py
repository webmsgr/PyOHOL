# insert setup.py here
# todo implement

from distutils.core import setup
from distutils.extension import Extension
import sys
import glob

if '--use-cython' in sys.argv:
    USE_CYTHON = True
    sys.argv.remove('--use-cython')
else:
    USE_CYTHON = False
ext = '.pyx' if USE_CYTHON else '.cpp'
exts = []

for file in glob.glob("OneLife/**/py_*"+ext) + glob.glob("minorGems/**/py_*"+ext):
    exts.append(Extension(file.replace("/",".").replace(ext,""),[file],language='c++',include_dirs=[]))


if USE_CYTHON:
    from Cython.Build import cythonize
    exts = cythonize(exts)

setup(
    ext_modules = exts
)
