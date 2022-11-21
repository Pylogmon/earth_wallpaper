from PySide6.QtCore import Qt, QSettings, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from earth_wallpaper.ui.UI_config import Ui_Config
from earth_wallpaper.utils.platformInfo import PlatformInfo
from earth_wallpaper import interfaces
import os


def _get_class_name_(name: str):
    for i in dir(interfaces):
        if getattr(interfaces, i).name() == name:
            return i


def trans(i: str) -> bool:
    if i == "true" or i == "True":
        return True
    if i == "false" or i == "False":
        return False


class Config(QWidget, Ui_Config):
    configChanged = Signal()

    def __init__(self):
        super(Config, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.config_path = PlatformInfo.config_path()
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setWindowIcon(QIcon(os.path.join(self.path, "resource/earth-wallpaper.png")))
        self.setupUi(self)
        self.initUI()
        self.check()
        self.read_config()
        self._update_layout_()
        self._connect_()
        self.show()

    def initUI(self):
        for i in dir(interfaces):
            if i[0] == '_':
                break
            name = getattr(interfaces, i).name()
            self.source.addItem(name)
        self.sorting.addItem("Relevance")
        self.sorting.addItem("Random")
        self.sorting.addItem("Date Added")
        self.sorting.addItem("Views")
        self.sorting.addItem("Favorites")
        self.sorting.addItem("Toplist")
        self.sorting.addItem("Hot")

    def _update_layout_(self):
        updateTimeGroup = [self.updateTime, self.updateTime_l]
        earthSizeGroup = [self.earthSize, self.earthSize_l]
        wallpaperDirGroup = [self.wallpaperDir, self.wallpaperDir_l, self.selectDir]
        wallpaperFileGroup = [self.wallpaperFile, self.wallpaperFile_l, self.selectFile]
        apikeyGroup = [self.apikey_l, self.apikey]
        categoriesGroup = [self.categories_l, self.General, self.Anime, self.People]
        purityGroup = [self.purity_l, self.SFW, self.Sketchy, self.NSFW]
        sortingGroup = [self.sorting_l, self.sorting]
        all_layout = [updateTimeGroup, earthSizeGroup, wallpaperDirGroup, wallpaperFileGroup, apikeyGroup,
                      categoriesGroup, purityGroup, sortingGroup]
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
        self.closeBtn.clicked.connect(self.close)
        self.applyBtn.clicked.connect(self.write_config)
        self.selectFile.clicked.connect(self.select_file)
        self.selectDir.clicked.connect(self.select_dir)

    def check(self):
        if os.path.exists(self.config_path):
            settings = QSettings(self.config_path, QSettings.IniFormat)
            if 'APP/apikey' not in settings.allKeys():
                self.set_default_config()
            else:
                return
        else:
            self.set_default_config()

    def set_default_config(self):
        settings = QSettings(self.config_path, QSettings.IniFormat)
        settings.beginGroup("APP")
        settings.setValue("wallpaperSource", "风云四号")
        settings.setValue("updateTime", 30)
        settings.setValue("earthSize", 60)
        settings.setValue("General", True)
        settings.setValue("Anime", False)
        settings.setValue("People", False)
        settings.setValue("SFW", True)
        settings.setValue("Sketchy", False)
        settings.setValue("NSFW", False)
        settings.setValue("sorting", "Random")
        settings.endGroup()

        settings.beginGroup("System")
        settings.setValue("proxy", 0)

        settings.setValue("proxyAdd", "")
        settings.setValue("proxyPort", "")
        settings.endGroup()

    def read_config(self):
        settings = QSettings(self.config_path, QSettings.IniFormat)

        settings.beginGroup("APP")
        self.source.setCurrentText(settings.value("wallpaperSource"))
        self.updateTime.setValue(int(settings.value("updateTime")))
        self.earthSize.setValue(int(settings.value("earthSize")))
        self.wallpaperDir.setText(settings.value("wallpaperDir"))
        self.wallpaperFile.setText(settings.value("wallpaperFile"))
        self.apikey.setText(settings.value("apikey"))
        # setting.value('General')
        # 返回的值有时候是str 'false'
        # 有时候是bool False
        # 猜测是因为从内存中读的是bool,从文件中读的是str
        self.General.setChecked(trans(str(settings.value("General"))))
        self.Anime.setChecked(trans(str(settings.value("Anime"))))
        self.People.setChecked(trans(str(settings.value("People"))))
        self.SFW.setChecked(trans(str(settings.value("SFW"))))
        self.Sketchy.setChecked(trans(str(settings.value("Sketchy"))))
        self.NSFW.setChecked(trans(str(settings.value("NSFW"))))
        self.sorting.setCurrentText(settings.value("sorting"))
        settings.endGroup()

        settings.beginGroup("System")
        if int(settings.value("proxy")) == 0:
            self.proxyNone.setChecked(True)
        elif int(settings.value("proxy")) == 1:
            self.proxyHttp.setChecked(True)
        else:
            self.proxySocks.setChecked(True)

        self.addEdit.setText(settings.value("proxyAdd"))
        self.portEdit.setText(settings.value("proxyPort"))
        settings.endGroup()

    def write_config(self):
        settings = QSettings(self.config_path, QSettings.IniFormat)
        settings.beginGroup("APP")
        settings.setValue("wallpaperSource", self.source.currentText())
        settings.setValue("updateTime", self.updateTime.value())
        settings.setValue("earthSize", self.earthSize.value())
        settings.setValue("wallpaperDir", self.wallpaperDir.text())
        settings.setValue("wallpaperFile", self.wallpaperFile.text())
        settings.setValue("apikey", self.apikey.text())
        settings.setValue("General", self.General.isChecked())
        settings.setValue("Anime", self.Anime.isChecked())
        settings.setValue("People", self.People.isChecked())
        settings.setValue("SFW", self.SFW.isChecked())
        settings.setValue("Sketchy", self.Sketchy.isChecked())
        settings.setValue("NSFW", self.NSFW.isChecked())
        settings.setValue("sorting", self.sorting.currentText())
        settings.endGroup()

        settings.beginGroup("System")
        if self.proxyNone.isChecked():
            settings.setValue("proxy", 0)
        elif self.proxyHttp.isChecked():
            settings.setValue("proxy", 1)
        else:
            settings.setValue("proxy", 2)

        settings.setValue("proxyAdd", self.addEdit.text())
        settings.setValue("proxyPort", self.portEdit.text())
        settings.endGroup()
        message = QMessageBox()
        QMessageBox.information(message, "设置", "设置保存成功！", QMessageBox.Yes)
        self.configChanged.emit()

    def select_dir(self):
        dir = QFileDialog.getExistingDirectory(self, "选择壁纸文件夹")
        self.wallpaperDir.setText(dir)

    def select_file(self):
        file = QFileDialog.getOpenFileName(self, "选择24h壁纸文件", "",
                                           "24h壁纸文件 (*.ddw *.zip);;")
        self.wallpaperFile.setText(file[0])
