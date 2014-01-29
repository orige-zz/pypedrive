from setuptools import setup

setup(
    name='pypedrive',
    version='0.1.1',
    license='MIT',

    author='Eduardo Orige',
    author_email='eduardo.orige@gmail.com',

    url='http://github.com/orige/pypedrive',
    download_url='http://github.com/orige/pypedrive/downloads',

    include_package_data=True,
    packages=['pypedrive'],
    zip_false=False,

    install_requires = ['requests',]
)
