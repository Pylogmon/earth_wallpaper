import dbus


class Cutefish(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        bus = dbus.SessionBus()
        settings = bus.get_object('com.cutefish.Settings', '/Theme')
        theme_interface = dbus.Interface(settings,
                                         dbus_interface='com.cutefish.Theme')
        theme_interface.setWallpaper(self.file)
