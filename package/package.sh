#/bin/bash
mkdir -p packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin
cp -r ../debian ./packageSpace/DEBIAN
cp ../build/earth-wallpaper ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/earth-wallpaper
cp -r ../build/scripts ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/scripts
cp -r ../build/template ./packageSpace/opt/apps/cn.huguoyang.earthwallpaper/files/bin/template

sed -i "s/Version: .*/Version: $(git describe --long 2>/dev/null | sed  's/\([^-]*-g\)/r\1/;s/-/./g')/g" packageSpace/DEBIAN/control && git describe --long 2>/dev/null || sed -i "s/Version: .*/Version: r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)/g"  packageSpace/DEBIAN/control

dpkg -b ./packageSpace earth-wallpaper-amd64.deb
