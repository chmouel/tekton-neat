#!/usr/bin/env python
"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = []

setup_requirements = ['pyyaml']

test_requirements = [
    'pytest>=3',
]

setup(
    author="Chmouel Boudjnah",
    author_email='chmouel@chmouel.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Export your tekton templates neatly",
    entry_points={
        'console_scripts': [
            'tekton-neat=tekton_neat.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tekton-neat',
    name='tekton-neat',
    packages=find_packages(include=['tekton_neat', 'tekton_neat.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/chmouel/tekton-neat',
    version='0.2.0',
    zip_safe=False,
)
