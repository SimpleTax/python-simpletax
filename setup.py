from distutils.core import setup

setup(
    name='python-simpletax',
    version='0.1.0',
    author='Celso Pinto',
    author_email='celso@gosimpletax.com',
    packages=['simpletax'],
    url='http://pypi.python.org/pypi/python-simpletax/',
    license='LICENSE.txt',
    description='Python API client to gosimpletax.com',
    long_description=open('README.markdown').read(),
    install_requires=[
        "requests-oauthlib == 0.3.2",
    ],
)
