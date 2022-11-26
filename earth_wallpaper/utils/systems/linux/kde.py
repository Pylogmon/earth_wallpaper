import dbus


class KDE(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        bus = dbus.SessionBus()
        shell = bus.get_object('org.kde.plasmashell', '/PlasmaShell')
        shell_interface = dbus.Interface(shell,
                                         dbus_interface='org.kde.PlasmaShell')
        shell_interface.evaluateScript(
            f"var allDesktops = desktops();print (allDesktops);for (i=0;i<allDesktops.length;i++) {{d = "
            f"allDesktops[i];d.wallpaperPlugin = \"org.kde.image\";d.currentConfigGroup = Array(\"Wallpaper\", "
            f"\"org.kde.image\", \"General\");d.writeConfig(\"Image\", \"file://{self.file}\")}} "
        )
