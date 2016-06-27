from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='geostatil',
    version=__version__,
    description="Detailed statistical data on any point in Israel",
    long_description="",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='cbs lamas statistics israel',
    author='Adam Kariv',
    author_email='adam@obudget.org',
    url='https://github.com/akariv/geostatil',
    license='MIT',
    packages=['geostatil'],
    package_dir={
        'geostatil': 'geostatil'
    },
    namespace_packages=[],
    package_data={
        'geostatil': ['data/*.json']
    },
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        'shapely',
        'pyproj',
        'geocoder',
    ],
    tests_require=[
    ],
)
