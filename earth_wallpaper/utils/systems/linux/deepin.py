import dbus
import os


class Deepin(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        primary_screen = os.popen("xrandr|grep 'connected primary'")
        primary_screen = primary_screen.read().splitlines()
        bus = dbus.SessionBus()
        appearance = bus.get_object('com.deepin.daemon.Appearance',
                                    '/com/deepin/daemon/Appearance')
        appearance_interface = dbus.Interface(
            appearance, dbus_interface='com.deepin.daemon.Appearance')
        for i in primary_screen:
            screen_name = i.split(" ")[0]
            appearance_interface.SetMonitorBackground(screen_name, self.file)
