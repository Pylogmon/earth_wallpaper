import win32api
import win32gui
import win32con


class Windows(object):

    def __init__(self, file):
        self.file = file

    def run(self):
        key = win32api.RegOpenKeyEx(win32con.HKEY_CURRENT_USER,
                                    "Control Panel\\Desktop", 0,
                                    win32con.KEY_SET_VALUE)
        win32api.RegSetValueEx(key, "WallpaperStyle", 0, win32con.REG_SZ,
                               "10")  # 2拉伸适应桌面，0桌面居中，10填充  拉伸会使一些图片变形
        win32api.RegSetValueEx(key, "TileWallpaper", 0, win32con.REG_SZ, "0")
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.file,
                                      win32con.SPIF_SENDWININICHANGE)
