import os

from setuptools import setup


requires = [
    'pyramid',
    'pyramid_jinja2',
    'sentry_sdk',
]


setup(
    name='ipxeboot',
    version='0.0',
    description='ipxeboot',
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Pyramid',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
    author='Łukasz Kostka',
    author_email='lukasz.kostka@netng.pl',
    keywords='web pyramid pylons',
    packages=[
        'ipxeboot',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)
