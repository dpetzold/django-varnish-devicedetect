# -*- coding: utf-8 -*-
from setuptools import setup


description = """\
A django package that allows easy identification of visitors'
browser, operating system and device information (mobile
phone, tablet or has touch capabilities).
"""

setup(
    name='django-varnish-devicedetect',
    version='0.1.0',
    author='Derrick Petzold',
    author_email='derrick@petzold.io',
    packages=['varnish_devicedetect'],
    url='https://github.com/dpetzold/django-varnish-devicedetect',
    license='MIT',
    description=description,
    # long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['django'],
    tests_requires=['mock'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
