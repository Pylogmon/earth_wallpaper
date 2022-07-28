import os


def set_wallpaper(file):
    DE = os.getenv('XDG_CURRENT_DESKTOP')
    if (DE == "Deepin"):
        primary_screen = os.popen("xrandr|grep 'connected primary'")
        primary_screen = primary_screen.read().split(" ")[0]
        dbus = f"qdbus com.deepin.daemon.Appearance /com/deepin/daemon/Appearance com.deepin.daemon.Appearance.SetMonitorBackground \"{primary_screen}\" \"{file}\""
        os.system(dbus)
    elif (DE == "KDE"):
        dbus = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}'"
        os.system(dbus)
    elif (DE == 'GNOME'):
        gs1 = "gsettings set org.gnome.desktop.background picture-uri {}".format(file)
        gs2 = "gsettings set org.gnome.desktop.background picture-uri-dark {}".format(file)
        os.system(gs1)
        os.system(gs2)
    else:
        print("该桌面环境暂不支持")
