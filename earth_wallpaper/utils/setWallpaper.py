from .platformInfo import PlatformInfo
import os


def set_wallpaper(file):
    sys = PlatformInfo().get_os()

    if sys == "Windows":
        import win32api, win32gui, win32con
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop", 0,
                                    win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ,
                               "10")  # 2拉伸适应桌面，0桌面居中，10填充  拉伸会使一些图片变形
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, file,
                                      win32con.SPIF_SENDWININICHANGE)

    elif sys == "Linux":
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
        elif de == "Cutefish":
            import dbus
            bus = dbus.SessionBus()
            settings = bus.get_object('com.cutefish.Settings', '/Theme')
            theme_interface = dbus.Interface(
                settings, dbus_interface='com.cutefish.Theme')
            theme_interface.setWallpaper(file)
        elif de == "KDE":
            import dbus
            bus = dbus.SessionBus()
            shell = bus.get_object('org.kde.plasmashell', '/PlasmaShell')
            shell_interface = dbus.Interface(
                shell, dbus_interface='org.kde.PlasmaShell')
            shell_interface.evaluateScript(
                f"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", \"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{file}\")}}"
            )
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
        elif de == 'MATE':
            gs = "gsettings set org.mate.background picture-filename {}".format(
                file)
            os.system(gs)
        elif de == 'LXQt' or de == 'LXDE':
            os.system("pcmanfm-qt -w {}".format(file))
            os.system("pcmanfm -w {}".format(file))
        else:
            print("该桌面环境暂不支持")
