import os


def set_wallpaper(file):
    de = os.getenv('XDG_CURRENT_DESKTOP')
    if de == "Deepin":
        import dbus
        primary_screen = os.popen("xrandr|grep 'connected primary'")
        primary_screen = primary_screen.read().splitlines()
        bus = dbus.SessionBus()
        appearance = bus.get_object('com.deepin.daemon.Appearance',
                                    '/com/deepin/daemon/Appearance')
        appearance_interface = dbus.Interface(
            appearance, dbus_interface='com.deepin.daemon.Appearance')
        for i in primary_screen:
            screen_name = i.split(" ")[0]
            appearance_interface.SetMonitorBackground(screen_name, file)
    elif de == "KDE":
        import dbus
        bus = dbus.SessionBus()
        shell = bus.get_object('org.kde.plasmashell', '/PlasmaShell')
        shell_interface = dbus.Interface(shell,
                                         dbus_interface='org.kde.PlasmaShell')
        shell_interface.evaluateScript(
            f"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}"
        )
    elif de == 'GNOME' or de == 'ubuntu:GNOME':
        gs1 = "gsettings set org.gnome.desktop.background picture-uri {}".format(file)
        gs2 = "gsettings set org.gnome.desktop.background picture-uri-dark {}".format(file)
        os.system(gs1)
        os.system(gs2)
    elif de == "XFCE":
        path = os.path.split(os.path.realpath(__file__))[0]
        os.system(path + "/xfce.sh {}".format(file))
    elif de == 'X-Cinnamon':
        gs = "gsettings set org.cinnamon.desktop.background picture-uri file://{}".format(file)
        os.system(gs)
    elif de == 'MATE':
        gs = "gsettings set org.mate.background picture-filename {}".format(file)
        os.system(gs)
    elif de =='LXQT':
        import dbus
        primary_screen = os.popen("xrandr|grep 'connected primary'")
        primary_screen = primary_screen.read().splitlines()
        bus = dbus.SessionBus()
        desktop = bus.get_object('org.freedesktop.portal.Desktop',
                                    '/org/freedesktop/portal/desktop')
        desktop_interface = dbus.Interface(
            desktop, dbus_interface='org.freedesktop.portal.Wallpaper')
        for i in primary_screen:
            screen_name = i.split(" ")[0]
            desktop_interface.SetWallpaperURI(screen_name, f'file://{file}')
    else:
        print("该桌面环境暂不支持")
