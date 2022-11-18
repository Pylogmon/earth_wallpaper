from setuptools import setup, find_packages
import platform


requires_list=[
    'Pillow',
    'PySide6',
    'requests',
    'setuptools',
]
if platform.system()=="Windows":
    requires_list.append('pywin32')

setup(
    name='earth-wallpaper',
    version='2.0.0',
    url='https://github.com/ambition-echo/earth_wallpaper',
    description='Simple and easy to use multifunctional wallpaper software',
    long_description='Simple and easy to use multifunctional wallpaper software 简单好用的多功能壁纸软件',
    author='ambition-echo',
    author_email='ambition_echo@outlook.com',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        'earth_wallpaper': ['resource/earth-wallpaper.png']
    },
    entry_points={
        'console_scripts': ['earth-wallpaper = earth_wallpaper.main:main']
    },
    requires=requires_list
)
