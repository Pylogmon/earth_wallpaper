import os


def set_wallpaper(file):
    de = os.getenv('XDG_CURRENT_DESKTOP')
    if de == "Deepin":
        primary_screen = os.popen("xrandr|grep 'connected primary'")
        primary_screen = primary_screen.read().splitlines()
        for i in primary_screen:
            screen_name = i.split(" ")[0]
            dbus = f"qdbus com.deepin.daemon.Appearance /com/deepin/daemon/Appearance " \
                   f"com.deepin.daemon.Appearance.SetMonitorBackground \"{screen_name}\" \"{file}\" "
            os.system(dbus)
    elif de == "KDE":
        dbus = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = " \
               f"desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[" \
               f"i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", " \
               f"\"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}' "
        os.system(dbus)
    elif de == 'GNOME' or de == 'ubuntu:GNOME':
        gs1 = "gsettings set org.gnome.desktop.background picture-uri {}".format(
            file)
        gs2 = "gsettings set org.gnome.desktop.background picture-uri-dark {}".format(
            file)
        os.system(gs1)
        os.system(gs2)
    elif de == "XFCE":
        path = os.path.split(os.path.realpath(__file__))[0]
        os.system(path + "/xfce.sh {}".format(file))
    elif de == 'X-Cinnamon':
        gs = "gsettings set org.cinnamon.desktop.background picture-uri file://{}".format(
            file)
        os.system(gs)
    else:
        print("该桌面环境暂不支持")
