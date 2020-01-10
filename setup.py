from setuptools import setup, find_packages
import os

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(here, 'deathbycaptcha', 'VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

with open(os.path.join(here, 'requirements.txt')) as f:
    requirements = []
    for line in f:
        line = line.strip()
        if line and not line.startswith('#'):
            requirements.append(line)

setup(
    name='deathbycaptcha',
    version=version,
    description='A library aims to support deathbycaptcha.',
    long_description=long_description,
    url='https://github.com/hyan15/python-deathbycaptcha',
    author='Neal Wong',
    author_email='qwang16@olivetuniversity.edu',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ],
    keywords='deathbycaptcha',
    packages=find_packages(exclude=('tests')),
    include_package_data=True,
    test_suite='tests',
    install_requires=requirements
)
