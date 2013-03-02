from distutils.core import setup

setup(
    name='django-freebase',
    version='0.1dev',
    author='Jonathan Hensley',
    author_email='jhensley2@gmail.com',
    packages=['freebase'],
    url='http://pypi.python.org/pypi/django-freebase/',
    license='LICENSE.txt',
    description='Freebasing in Django.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.5",
    ],
)