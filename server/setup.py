"""zc.buildout language server
"""

from os import path

from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

with open(path.join(here, 'CHANGELOG.md'), encoding='utf-8') as f:
  long_description += f.read()

setup(
    name='mylang.languageserver',
    version='0.5.0',
    description='A language server for mylang',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Framework :: Buildout',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    keywords='mylang languageserver',
    packages=['mylangcompiler'],
    python_requires='>=3.6.*',
    install_requires=[
        'pygls >= 0.10.1',
        'requests',
        'zc.buildout',
    ],
    extras_require={
        'test': [
            'coverage',
            'pytest',
            'pytest-asyncio',
            'responses',
        ],
    },
    entry_points={
        'console_scripts': [
            'buildoutls=buildoutls.cli:main',
        ],
    },
)
