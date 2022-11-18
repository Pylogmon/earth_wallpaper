from PySide6.QtCore import Qt, QUrl
from PySide6.QtGui import QIcon, QDesktopServices
from PySide6.QtWidgets import QWidget, QApplication
from earth_wallpaper.ui.UI_about import Ui_About
import os


def get_version():
    return "2.0.2"


class About(QWidget, Ui_About):

    def __init__(self):
        super(About, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setWindowIcon(QIcon(os.path.join(self.path, "resource/earth-wallpaper.png")))
        self.setupUi(self)
        self.initUI()
        self._connect_()
        self.show()

    def initUI(self):
        self.version.setText(get_version())

    def _connect_(self):
        self.aboutQt.clicked.connect(QApplication.aboutQt)
        self.checkUpdate.clicked.connect(self.check_update)

    def check_update(self):
        QDesktopServices.openUrl(QUrl("https://github.com/ambition-echo/earth_wallpaper/releases"))
