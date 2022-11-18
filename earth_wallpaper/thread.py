from PySide6.QtCore import QThread
from earth_wallpaper.utils.setWallpaper import set_wallpaper
from earth_wallpaper.utils.platformInfo import PlatformInfo
from earth_wallpaper import interfaces


def get_class_name(name: str):
    for i in dir(interfaces):
        if getattr(interfaces, i).name() == name:
            return i


class Thread(QThread):

    def __init__(self, name):
        super(Thread, self).__init__()
        self.class_name = get_class_name(name)
        self.flag = True

    def run(self):
        x = getattr(interfaces, self.class_name)()
        print(f"Start run {x.name()}...")
        if x.name() == "本地壁纸":
            img_path = x.run()
            set_wallpaper(img_path)
        else:
            img = x.run()
            if self.flag:
                PlatformInfo().check()
                with open(x.download_path, "wb") as f:
                    f.write(img)
                set_wallpaper(x.download_path)
        print("Run completed!")

    def stop(self):
        self.flag = False
