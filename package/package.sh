#/bin/bash
mkdir -p packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin
cp ../build/earth-wallpaper ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/earth-wallpaper
cp -r ../build/scripts ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/scripts
cp -r ../build/template ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/template

sed -i "s/Version: .*/Version: $(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')/g" packageSpace/DEBIAN/control
sed -i "s/\"version\": .*/\"version\": \"$(git describe --tags |  sed  's/\([^-]*-g\)/r\1/;s/-/./g')\",/g" packageSpace/opt/apps/cn.huguoyang.earthwallpaper/info

chmod 755 ./packageSpace/DEBIAN
chmod 755 ./packageSpace/DEBIAN/control
dpkg -b ./packageSpace earth-wallpaper-deepin-amd64.deb

cp -r ../DEBIAN/ ./packageSpace/
chmod 755 ./packageSpace/DEBIAN/postinst
chmod 755 ./packageSpace/DEBIAN/postrm
dpkg -b ./packageSpace earth-wallpaper-other-amd64.deb