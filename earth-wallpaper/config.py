from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget
from ui.UI_config import Ui_Config
import interfaces
import os


def _get_class_name_(name: str):
    for i in dir(interfaces):
        if getattr(interfaces, i).name() == name:
            return i


class Config(QWidget, Ui_Config):

    def __init__(self):
        print(dir(interfaces))
        super(Config, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setWindowIcon(QIcon(os.path.join(self.path, "resource/earth-wallpaper.png")))
        self.setupUi(self)
        self.initUI()
        self._update_layout_()
        self._connect_()
        self.show()

    def initUI(self):
        for i in dir(interfaces):
            if i[0] == '_':
                break
            name = getattr(interfaces, i).name()
            self.source.addItem(name)
            print(_get_class_name_(name))

    def _update_layout_(self):
        updateTimeGroup = [self.updateTime, self.updateTime_l]
        earthSizeGroup = [self.earthSize, self.earthSize_l]
        wallpaperDirGroup = [self.wallpaperDir, self.wallpaperDir_l, self.selectDir]
        wallpaperFileGroup = [self.wallpaperFile, self.wallpaperFile_l, self.selectFile]
        all_layout = [updateTimeGroup, earthSizeGroup, wallpaperDirGroup, wallpaperFileGroup]
        class_name = _get_class_name_(self.source.currentText())
        layout_list = getattr(interfaces, class_name).layout()
        for i in all_layout:
            for j in i:
                j.hide()
        for i in layout_list:
            for j in locals()[i]:
                j.show()

    def _connect_(self):
        self.source.currentIndexChanged.connect(self._update_layout_)
