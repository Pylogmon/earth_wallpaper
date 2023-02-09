# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QWidget)

class Ui_About(object):
    def setupUi(self, About):
        if not About.objectName():
            About.setObjectName(u"About")
        About.resize(283, 266)
        self.gridLayout = QGridLayout(About)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 0, 1, 1)

        self.label = QLabel(About)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"font: 700 20pt;")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.version = QLabel(About)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.version, 2, 0, 1, 1)

        self.aboutQt = QPushButton(About)
        self.aboutQt.setObjectName(u"aboutQt")

        self.gridLayout.addWidget(self.aboutQt, 3, 0, 1, 1)

        self.checkUpdate = QPushButton(About)
        self.checkUpdate.setObjectName(u"checkUpdate")

        self.gridLayout.addWidget(self.checkUpdate, 4, 0, 1, 1)

        self.label_2 = QLabel(About)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.gridLayout.addWidget(self.label_2, 5, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 78, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)


        self.retranslateUi(About)

        QMetaObject.connectSlotsByName(About)
    # setupUi

    def retranslateUi(self, About):
        About.setWindowTitle(QCoreApplication.translate("About", u"\u5173\u4e8e", None))
        self.label.setText(QCoreApplication.translate("About", u"Earth Wallpaper", None))
        self.version.setText(QCoreApplication.translate("About", u"1.3.0", None))
        self.aboutQt.setText(QCoreApplication.translate("About", u"Qt", None))
        self.checkUpdate.setText(QCoreApplication.translate("About", u"\u68c0\u67e5\u66f4\u65b0", None))
        self.label_2.setText(QCoreApplication.translate("About", u"<html><head/><body><p>\u6781\u72d0: <a href=\"https://jihulab.com/ambition-echo/earth_wallpaper\"><span\n"
"                            style=\" text-decoration: underline; color:#255fff;\">earth_wallpaper</span></a></p><p>Github:\n"
"                            <a href=\"https://github.com/ambition-echo/earth_wallpaper\"><span style=\"\n"
"                            text-decoration: underline; color:#255fff;\">earth_wallpaper</span></a></p><p>Email:\n"
"                            <a href=\"mailto://ambition_echo@outlook.com\"><span style=\"\n"
"                            text-decoration: underline; color:#255fff;\">ambition_echo@outlook.com</span></a></p></body></html>\n"
"                        ", None))
    # retranslateUi

