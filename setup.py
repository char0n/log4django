# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

import log4django


setup(
    name='log4django',
    version=log4django.get_version(),
    description='log4django is full features logging platform for django applications.',
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    author=u'Vladimír Gorej',
    author_email='gorej@codescale.net',
    url='http://www.codescale.net/en/community#log4django',
    download_url='http://github.com/CodeScaleInc/log4django/tarball/master',
    license='BSD',
    keywords='logging, django, log, logs',
    packages=find_packages('.'),
    include_package_data=True,
    install_requires = [
        'Django', 'django-model-utils', 'django-tastypie',
        'jsonpath', 'jsonpickle', 'mimeparse', 'python-dateutil',
        'django-log-request-id', 'south'
    ],
    extras_require = {
        'gearman': ['gearman==dev', 'django-gearman-commands==dev'],
        'tests': ['mock']
    },
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Browsers'
    ],
    dependency_links = [
        'git+git://github.com/Yelp/python-gearman.git#egg=gearman-dev',
        'git+git://github.com/CodeScaleInc/django-gearman-commands.git#egg=django_gearman_commands-dev',
    ]
)
