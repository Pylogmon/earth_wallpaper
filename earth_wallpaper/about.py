from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QApplication, QMessageBox
from earth_wallpaper.ui.UI_about import Ui_About
import requests
import logging
import json
import os

logger = logging.getLogger(__name__)


def get_version():
    return "2.0.9"


def compare(remote, local):
    if int(remote[0]) > int(local[0]):
        return True
    elif int(remote[1]) > int(local[1]):
        return True
    elif int(remote[2]) > int(local[2]):
        return True
    else:
        return False


def check_update():
    logger.info("检查软件更新")
    url = "https://api.github.com/repos/ambition-echo/earth_wallpaper/tags"
    tags_json = requests.get(url)
    if tags_json.ok:
        remote_tag = json.loads(tags_json.content.decode())[0]["name"]
        local_tag = get_version().split('.')
        if compare(remote_tag.split('.'), local_tag):
            logger.info(f"新版本可用，最新版本为{remote_tag}")
            message = QMessageBox()
            QMessageBox.information(message, "有可用更新", f"最新版本为{remote_tag}，请及时更新版本",
                                    QMessageBox.Yes)
            return True
        else:
            logger.info("软件为最新版本")
            return False


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
        self.checkUpdate.clicked.connect(self.check)

    @staticmethod
    def check(self):

        message = QMessageBox()
        if check_update():
            pass
        else:
            QMessageBox.information(message, "无可用更新", f"当前版本为最新版本，无需更新", QMessageBox.Yes)
