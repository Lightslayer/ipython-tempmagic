try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import io
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the relevant file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = [
    'jupyter>=1.0.0',
]

setup(
    name='ipython-tempmagic',
    version='0.0.1',
    description='Temporary file magic IPython',
    long_description=long_description,
    url='https://github.com/tkf/ipython-tempmagic',

    # Author details
    author='Takafumi Arakaki',
    author_email='aka.tkf@gmail.com',
    maintainer='Liam Deacon',
    maintainer_email='liam.m.deacon@gmail.com',

    # Choose your license
    license='',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Topic :: Text Processing :: Markup :: HTML',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='ipython jupyter notebook tempfile tempdir',

    packages={'tempmagic':''},
    py_modules=['tempmagic.py'],
    install_requires=install_requires,
)
