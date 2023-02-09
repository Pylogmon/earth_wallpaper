from PySide6.QtWidgets import QWidget, QMessageBox, QFileDialog
from earth_wallpaper.utils.platformInfo import PlatformInfo
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
from earth_wallpaper.ui.UI_config import Ui_Config
from PySide6.QtCore import Qt, QSettings, Signal
from earth_wallpaper import interfaces
import logging
import shutil
import os

logger = logging.getLogger(__name__)


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
        self.setWindowIcon(
            QIcon(os.path.join(self.path, "resource/earth-wallpaper.png")))
        self.setupUi(self)
        self.initUI()
        self.check()
        self.read_config()
        self.update_layout()
        self.init_connect()
        self.show()

    def initUI(self):
        for i in dir(interfaces):
            if i[0] == '_':
                break
            name = getattr(interfaces, i).name()
            logger.info(f"获取到可用接口: {name}")
            self.source.addItem(name)
        sorting_list = [
            "Relevance", "Random", "Date Added", "Views", "Favorites",
            "Toplist", "Hot"
        ]
        for i in sorting_list:
            self.sorting.addItem(i)
        atleast_list = ["1920x1080", "2160x1440", "3840x2160"]
        for i in atleast_list:
            self.atleast.addItem(i)
        self.init_color_select()
        self.get_cache_size()

    def update_layout(self):
        updateTimeGroup = [self.updateTime, self.updateTime_l]
        earthSizeGroup = [self.earthSize, self.earthSize_l]
        wallpaperDirGroup = [
            self.wallpaperDir, self.wallpaperDir_l, self.selectDir
        ]
        wallpaperFileGroup = [
            self.wallpaperFile, self.wallpaperFile_l, self.selectFile
        ]
        apikeyGroup = [self.apikey_l, self.apikey]
        categoriesGroup = [
            self.categories_l, self.General, self.Anime, self.People
        ]
        purityGroup = [self.purity_l, self.SFW, self.Sketchy, self.NSFW]
        sortingGroup = [self.sorting_l, self.sorting]
        searchkeyGroup = [self.searchkey_l, self.searchkey]
        colorGroup = [self.color_l, self.color]
        atleastGroup = [self.atleast_l, self.atleast]
        all_layout = [
            updateTimeGroup, earthSizeGroup, wallpaperDirGroup,
            wallpaperFileGroup, apikeyGroup, categoriesGroup, purityGroup,
            sortingGroup, searchkeyGroup, colorGroup, atleastGroup
        ]

        class_name = _get_class_name_(self.source.currentText())
        layout_list = getattr(interfaces, class_name).layout()

        for i in all_layout:
            for j in i:
                j.hide()
        for i in layout_list:
            for j in locals()[i]:
                j.show()
        self.resize(1, 1)

    def init_connect(self):
        self.source.currentIndexChanged.connect(self.update_layout)
        self.closeBtn.clicked.connect(self.close)
        self.applyBtn.clicked.connect(self.write_config)
        self.selectFile.clicked.connect(self.select_file)
        self.selectDir.clicked.connect(self.select_dir)
        self.clearCache.clicked.connect(self.clear_cache)

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
        settings.setValue("color", "不选择")
        settings.setValue("atleast", "1920x1080")
        settings.endGroup()

        settings.beginGroup("System")
        settings.setValue("proxy", 0)

        settings.setValue("proxyAdd", "")
        settings.setValue("proxyPort", "")
        settings.endGroup()
        logger.info("写入默认设置")

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
        self.searchkey.setText(settings.value("searchkey"))
        self.color.setCurrentText(settings.value("color"))
        self.atleast.setCurrentText(settings.value("atleast"))
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
        self.scripts.setText(settings.value("scripts"))
        settings.endGroup()
        logger.info("读取设置")

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
        settings.setValue("searchkey", self.searchkey.text())
        settings.setValue("color", self.color.currentText())
        settings.setValue("atleast", self.atleast.currentText())
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
        settings.setValue("scripts", self.scripts.text())
        settings.endGroup()
        logger.info("写入设置")
        message = QMessageBox()
        QMessageBox.information(message, "设置", "设置保存成功！", QMessageBox.Yes)
        self.configChanged.emit()

    def select_dir(self):
        wallpaper_dir = QFileDialog.getExistingDirectory(self, "选择壁纸文件夹")
        logger.info(f"获取到文件夹地址{wallpaper_dir}")
        self.wallpaperDir.setText(wallpaper_dir)

    def select_file(self):
        file = QFileDialog.getOpenFileName(self, "选择24h壁纸文件", "",
                                           "24h壁纸文件 (*.ddw *.zip);;")
        logger.info(f"获取到文件地址{file}")
        self.wallpaperFile.setText(file[0])

    def clear_cache(self):
        cache = PlatformInfo.download_dir()
        if os.path.exists(cache):
            shutil.rmtree(cache)
            logger.info(f"删除缓存目录: {cache}")
        message = QMessageBox()
        QMessageBox.information(message, "清理缓存", "已删除全部缓存壁纸", QMessageBox.Yes)
        self.get_cache_size()

    def init_color_select(self):
        pix = QPixmap(16, 16)
        painter = QPainter(pix)
        color_list = [
            '#660000', '#990000', '#cc0000', '#cc3333', '#ea4c88', '#993399',
            '#663399', '#333399', '#0066cc', '#0099cc', '#66cccc', '#77cc33',
            '#669900', '#336600', '#666600', '#999900', '#cccc33', '#ffff00',
            '#ffcc33', '#ff9900', '#ff6600', '#cc6633', '#996633', '#663300',
            '#000000', '#999999', '#cccccc', '#ffffff', '#424153'
        ]
        for i in color_list:
            painter.fillRect(0, 0, 16, 16, QColor(i))
            self.color.addItem(QIcon(pix), i)
        self.color.addItem("不选择")
        painter.end()
        self.color.setFont("MonoSpace")

    def get_cache_size(self):
        unit_list = ['B', 'KB', 'MB', 'GB']
        cache_size = 0
        unit = 0
        cache = PlatformInfo.download_dir()
        if not os.path.exists(cache):
            self.clearCache.setText(f"删除缓存({cache_size} {unit_list[unit]})")
        else:
            for r, dirs, files in os.walk(cache):
                for i in files:
                    cache_size += os.path.getsize(os.path.join(r, i))
            while (cache_size >= 1024):
                cache_size = cache_size / 1024
                unit += 1
            self.clearCache.setText(
                f"删除缓存({round(cache_size,2)} {unit_list[unit]})")
