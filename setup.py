from codecs     import open
from inspect    import getsource
from os.path    import abspath, dirname, join
from setuptools import find_packages, setup

here = abspath(dirname(getsource(lambda:0)))

with open(join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name             = 'fingui',
      version          = '0.2.2',
      description      = long_description.splitlines()[2][1:-1],
      long_description = long_description,
      url              = 'https://github.com/TaylorSMarks/FinGUI',
      author           = 'Taylor Marks',
      author_email     = 'taylor@marksfam.com',
      license          = 'MIT',
      classifiers      = ['Development Status :: 1 - Planning',
                          'Intended Audience :: Developers',
                          'License :: OSI Approved :: MIT License',
                          'Operating System :: OS Independent',
                          'Programming Language :: Python :: 2',
                          'Programming Language :: Python :: 2.6',
                          'Programming Language :: Python :: 2.7',
                          'Topic :: Software Development :: Libraries :: Application Frameworks'],
      keywords         = 'gui tkinter ui ux widget widgets wrapper',
      packages         = find_packages())
