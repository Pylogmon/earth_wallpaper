#!/bin/bash
sed -i "s/return \".*/return \"$(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')\"/g" earth_wallpaper/about.py
python3 ./setup.py sdist bdist_wheel
# twine upload ./dist/*
