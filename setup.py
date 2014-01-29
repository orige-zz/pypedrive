from setuptools import setup

setup(
    name='pypedrive',
    version='0.1.2',
    license='MIT',

    author='Eduardo Orige',
    author_email='eduardo.orige@gmail.com',

    description='Light API for pipedrive.com',
    keywords='light pipedrive api',

    url='http://github.com/orige/pypedrive',
    download_url='http://github.com/orige/pypedrive/downloads',

    include_package_data=True,
    packages=['pypedrive'],
    zip_false=False,

    install_requires = ['requests',]
)
