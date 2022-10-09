from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QWidget
from .ui.UI_about import Ui_About
import os


class About(QWidget, Ui_About):

    def __init__(self):
        super(About, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.path = os.path.split(os.path.realpath(__file__))[0]
        self.setWindowIcon(QIcon(os.path.join(self.path, "../resource/earth-wallpaper.png")))
        self.setupUi(self)
        self.initUI()
        self._connect_()
        self.show()

    def initUI(self):
        self.version.setText("1.9.0")

    def _connect_(self):
        pass
