#!/bin/bash
mkdir -p packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/
cp -r ../earth-wallpaper ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin

sed -i "s/Version: .*/Version: $(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')/g" packageSpace/DEBIAN/control
sed -i "s/\"version\": .*/\"version\": \"$(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')\",/g" packageSpace/opt/apps/cn.huguoyang.earthwallpaper/info
sed -i "s/1.9.0/$(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')/g" packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/about.py
chmod 755 ./packageSpace/DEBIAN
chmod 755 ./packageSpace/DEBIAN/control
dpkg -b ./packageSpace earth-wallpaper-deepin-amd64.deb

cp -r ../DEBIAN/ ./packageSpace/
chmod 755 ./packageSpace/DEBIAN/postinst
chmod 755 ./packageSpace/DEBIAN/postrm
dpkg -b ./packageSpace earth-wallpaper-other-amd64.deb
