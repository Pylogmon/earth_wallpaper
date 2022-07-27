import os


def set_wallpaper(file):
    DE = os.getenv('XDG_CURRENT_DESKTOP')
    if (DE == "Deepin"):
        os.system("export primary_screen=($(xrandr|grep 'connected primary'))")
        primary_screen = os.getenv('primary_screen')

        dbus = f"qdbus com.deepin.daemon.Appearance /com/deepin/daemon/Appearance com.deepin.daemon.Appearance.SetMonitorBackground \"{primary_screen}\" \"{file}\""

        os.system(dbus)
    elif (DE == "KDE"):
        print(file)
        dbus = f"qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript 'var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}'"
        os.system(dbus)
    else:
        print("该桌面环境暂不支持")