#/bin/bash
mkdir -p package_space/opt/earth_wallpaper
cp -r ../debian ./package_space/DEBIAN
cp ../build/earth_wallpaper ./package_space/opt/earth_wallpaper/earth_wallpaper
cp -r ../build/scripts ./package_space/opt/earth_wallpaper/scripts
cp -r ../build/template ./package_space/opt/earth_wallpaper/template
cp ../resource/icon.png ./package_space/opt/earth_wallpaper/icon.png
cp -r ./usr ././package_space/usr
sed -i "s/Version: .*/Version: $(git describe --long 2>/dev/null | sed  's/\([^-]*-g\)/r\1/;s/-/./g')/g" package_space/DEBIAN/control && git describe --long 2>/dev/null || sed -i "s/Version: .*/Version: r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)/g"  package_space/DEBIAN/control

chmod 755 package_space/DEBIAN/postinst
chmod 755 package_space/DEBIAN/postrm
dpkg -b ./package_space earth-wallpaper-amd64.deb
