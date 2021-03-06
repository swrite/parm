__doc__ = """
=====================
Par 
=====================

:Author: Limodou <limodou@gmail.com>

.. contents:: 

About Parm
----------------

Parm can be used to convert markdown files to  html pages. It'll use par module to parse markdown. 
The features are:

* Topic content page support
* Bootstrap 2.1.1 css framework based

Requirement
----------------

* par https://github.com/limodou/par

Installation
----------------

```
pip install par
pip install parm
```

Usage
-------------

```
parm --help
parm --version
parm -d output_path
```

License
------------

Parm is released under BSD license. 

"""

from setuptools import setup
from setuptools.command import build_py as b
import os

#remove build and dist directory
import shutil
if os.path.exists('build'):
    shutil.rmtree('build')
if os.path.exists('dist'):
    shutil.rmtree('dist')

def copy_dir(self, package, src, dst):
    self.mkpath(dst)
    for r in os.listdir(src):
        if r in ['.svn', '_svn']:
            continue
        fpath = os.path.join(src, r)
        if os.path.isdir(fpath):
            copy_dir(self, package + '.' + r, fpath, os.path.join(dst, r))
        else:
            ext = os.path.splitext(fpath)[1]
            if ext in ['.pyc', '.pyo', '.bak', '.tmp']:
                continue
            target = os.path.join(dst, r)
            self.copy_file(fpath, target)

def find_dir(self, package, src):
    for r in os.listdir(src):
        if r in ['.svn', '_svn']:
            continue
        fpath = os.path.join(src, r)
        if os.path.isdir(fpath):
            for f in find_dir(self, package + '.' + r, fpath):
                yield f
        else:
            ext = os.path.splitext(fpath)[1]
            if ext in ['.pyc', '.pyo', '.bak', '.tmp']:
                continue
            yield fpath

def build_package_data(self):
    for package in self.packages or ():
        src_dir = self.get_package_dir(package)
        build_dir = os.path.join(*([self.build_lib] + package.split('.')))
        copy_dir(self, package, src_dir, build_dir)
setattr(b.build_py, 'build_package_data', build_package_data)

def get_source_files(self):
    filenames = []
    for package in self.packages or ():
        src_dir = self.get_package_dir(package)
        filenames.extend(list(find_dir(self, package, src_dir)))
    return filenames
setattr(b.build_py, 'get_source_files', get_source_files)

import parm

setup(name='parm',
    version=parm.__version__,
    description="Markdown to html convertor tool",
    long_description=__doc__,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
    ],
    packages = ['parm'],
    platforms = 'any',
    keywords='markdown convertor',
    author=parm.__author__,
    author_email=parm.__author_email__,
    url=parm.__url__,
    license=parm.__license__,
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'parm = parm:main',
        ],
    },
)
