from setuptools import setup, find_packages

setup(
    name='lgtm',
    version='1.0.0',
    packages=find_packages(exclude=('tests',)),
    include_package_data=True,
    install_requires=[
        'Click',
        'Pillow',
        'requests',
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli',
        ],
    },
)