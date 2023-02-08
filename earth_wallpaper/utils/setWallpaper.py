from PySide6.QtCore import QSettings, QStandardPaths
from .platformInfo import PlatformInfo
import logging
import os

logger = logging.getLogger(__name__)


def is_custom(file):
    config_dir = QStandardPaths.writableLocation(QStandardPaths.ConfigLocation)
    config_path = os.path.join(config_dir,
                               "earth-wallpaper/earth-wallpaper.conf")
    settings = QSettings(config_path, QSettings.IniFormat)
    scripts = settings.value("System/scripts")
    if not len(scripts) == 0:
        os.system(f"{scripts} {file}")
        return True
    else:
        False


def set_wallpaper(file):
    if is_custom(file):
        return

    sys = PlatformInfo().get_os()
    logger.info(f"当前系统为{sys}")

    if sys == "WINDOWS":
        from .systems.windows.windows import Windows
        x = Windows(file)
        x.run()

    if sys == "LINUX":
        from .systems.linux.cutefish import Cutefish
        from .systems.linux.cinnamon import Cinnamon
        from .systems.linux.deepin import Deepin
        from .systems.linux.gnome import Gnome
        from .systems.linux.xfce import XFCE
        from .systems.linux.mate import MATE
        from .systems.linux.lxqt import LXQT
        from .systems.linux.lxde import LXDE
        from .systems.linux.kde import KDE

        de = os.getenv('XDG_CURRENT_DESKTOP')
        logger.info(f"当前桌面环境为{de}")
        de_list = {
            "X-Cinnamon": Cinnamon,
            "ubuntu:Gnome": Gnome,
            "ubuntu:GNOME": Gnome,
            "GNOME": Gnome,
            "Cutefish": Cutefish,
            "Deepin": Deepin,
            "Gnome": Gnome,
            "XFCE": XFCE,
            "MATE": MATE,
            "LXQT": LXQT,
            "LXDE": LXDE,
            "KDE": KDE
        }
        x = de_list[de](file)
        x.run()
