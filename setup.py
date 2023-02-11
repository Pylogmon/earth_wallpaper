#!/bin/python3
from setuptools import setup, find_packages
from earth_wallpaper.about import get_version

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='earth-wallpaper',
    version=get_version(),
    url='https://github.com/Pylogmon/earth_wallpaper',
    description='Simple and easy to use multifunctional wallpaper software 简单好用的多功能壁纸软件',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="GPLv3",
    author='Pylogmon',
    author_email='pylogmon@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'earth_wallpaper': ['resource/earth-wallpaper.png']
    },
    entry_points={
        'console_scripts': ['earth-wallpaper = earth_wallpaper.main:main']
    },
    install_requires=[
        'Pillow',
        'PySide6',
        'requests',
        'pysocks',
        'dbus-python; platform_system == "Linux"',
        'pywin32; platform_system == "Windows"'
    ]
)
