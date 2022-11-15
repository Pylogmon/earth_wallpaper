# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QRadioButton, QSizePolicy, QSpacerItem, QSpinBox,
    QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(308, 398)
        self.gridLayout_3 = QGridLayout(Config)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.SystemSettings = QGroupBox(Config)
        self.SystemSettings.setObjectName(u"SystemSettings")
        self.gridLayout_2 = QGridLayout(self.SystemSettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.proxyTypeGroup = QHBoxLayout()
        self.proxyTypeGroup.setObjectName(u"proxyTypeGroup")
        self.proxy_l = QLabel(self.SystemSettings)
        self.proxy_l.setObjectName(u"proxy_l")

        self.proxyTypeGroup.addWidget(self.proxy_l)

        self.proxyNone = QRadioButton(self.SystemSettings)
        self.proxyNone.setObjectName(u"proxyNone")
        self.proxyNone.setChecked(True)

        self.proxyTypeGroup.addWidget(self.proxyNone)

        self.proxyHttp = QRadioButton(self.SystemSettings)
        self.proxyHttp.setObjectName(u"proxyHttp")

        self.proxyTypeGroup.addWidget(self.proxyHttp)

        self.proxySocks = QRadioButton(self.SystemSettings)
        self.proxySocks.setObjectName(u"proxySocks")

        self.proxyTypeGroup.addWidget(self.proxySocks)


        self.gridLayout_2.addLayout(self.proxyTypeGroup, 0, 0, 1, 1)

        self.addGroup = QHBoxLayout()
        self.addGroup.setObjectName(u"addGroup")
        self.add_l = QLabel(self.SystemSettings)
        self.add_l.setObjectName(u"add_l")

        self.addGroup.addWidget(self.add_l)

        self.addEdit = QLineEdit(self.SystemSettings)
        self.addEdit.setObjectName(u"addEdit")

        self.addGroup.addWidget(self.addEdit)

        self.port_l = QLabel(self.SystemSettings)
        self.port_l.setObjectName(u"port_l")

        self.addGroup.addWidget(self.port_l)

        self.portEdit = QLineEdit(self.SystemSettings)
        self.portEdit.setObjectName(u"portEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.portEdit.sizePolicy().hasHeightForWidth())
        self.portEdit.setSizePolicy(sizePolicy)
        self.portEdit.setMinimumSize(QSize(20, 0))

        self.addGroup.addWidget(self.portEdit)


        self.gridLayout_2.addLayout(self.addGroup, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.SystemSettings, 1, 0, 1, 3)

        self.applySpacer = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.applySpacer, 2, 0, 1, 1)

        self.applyBtn = QPushButton(Config)
        self.applyBtn.setObjectName(u"applyBtn")

        self.gridLayout_3.addWidget(self.applyBtn, 2, 1, 1, 1)

        self.closeBtn = QPushButton(Config)
        self.closeBtn.setObjectName(u"closeBtn")

        self.gridLayout_3.addWidget(self.closeBtn, 2, 2, 1, 1)

        self.AppSettings = QGroupBox(Config)
        self.AppSettings.setObjectName(u"AppSettings")
        self.gridLayout = QGridLayout(self.AppSettings)
        self.gridLayout.setObjectName(u"gridLayout")
        self.source_l = QLabel(self.AppSettings)
        self.source_l.setObjectName(u"source_l")

        self.gridLayout.addWidget(self.source_l, 0, 0, 1, 2)

        self.source = QComboBox(self.AppSettings)
        self.source.setObjectName(u"source")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.source.sizePolicy().hasHeightForWidth())
        self.source.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.source, 0, 2, 1, 2)

        self.updateTime_l = QLabel(self.AppSettings)
        self.updateTime_l.setObjectName(u"updateTime_l")

        self.gridLayout.addWidget(self.updateTime_l, 1, 0, 1, 2)

        self.updateTime = QSpinBox(self.AppSettings)
        self.updateTime.setObjectName(u"updateTime")
        self.updateTime.setMinimum(1)
        self.updateTime.setMaximum(1440)
        self.updateTime.setValue(30)

        self.gridLayout.addWidget(self.updateTime, 1, 2, 1, 2)

        self.earthSize_l = QLabel(self.AppSettings)
        self.earthSize_l.setObjectName(u"earthSize_l")

        self.gridLayout.addWidget(self.earthSize_l, 2, 0, 1, 2)

        self.earthSize = QSpinBox(self.AppSettings)
        self.earthSize.setObjectName(u"earthSize")
        self.earthSize.setMinimum(20)
        self.earthSize.setMaximum(100)

        self.gridLayout.addWidget(self.earthSize, 2, 2, 1, 2)

        self.wallpaperDir_l = QLabel(self.AppSettings)
        self.wallpaperDir_l.setObjectName(u"wallpaperDir_l")

        self.gridLayout.addWidget(self.wallpaperDir_l, 3, 0, 1, 2)

        self.wallpaperDir = QLineEdit(self.AppSettings)
        self.wallpaperDir.setObjectName(u"wallpaperDir")

        self.gridLayout.addWidget(self.wallpaperDir, 3, 2, 1, 1)

        self.selectDir = QPushButton(self.AppSettings)
        self.selectDir.setObjectName(u"selectDir")
        self.selectDir.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.selectDir, 3, 3, 1, 1)

        self.wallpaperFile_l = QLabel(self.AppSettings)
        self.wallpaperFile_l.setObjectName(u"wallpaperFile_l")

        self.gridLayout.addWidget(self.wallpaperFile_l, 4, 0, 1, 1)

        self.wallpaperFile = QLineEdit(self.AppSettings)
        self.wallpaperFile.setObjectName(u"wallpaperFile")

        self.gridLayout.addWidget(self.wallpaperFile, 4, 1, 1, 2)

        self.selectFile = QPushButton(self.AppSettings)
        self.selectFile.setObjectName(u"selectFile")
        self.selectFile.setMinimumSize(QSize(80, 0))

        self.gridLayout.addWidget(self.selectFile, 4, 3, 1, 1)


        self.gridLayout_3.addWidget(self.AppSettings, 0, 0, 1, 3)


        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"\u8bbe\u7f6e", None))
        self.SystemSettings.setTitle(QCoreApplication.translate("Config", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.proxy_l.setText(QCoreApplication.translate("Config", u"\u7f51\u7edc\u4ee3\u7406\uff1a", None))
        self.proxyNone.setText(QCoreApplication.translate("Config", u"\u65e0", None))
        self.proxyHttp.setText(QCoreApplication.translate("Config", u"http", None))
        self.proxySocks.setText(QCoreApplication.translate("Config", u"socks", None))
        self.add_l.setText(QCoreApplication.translate("Config", u"\u5730\u5740\uff1a", None))
        self.port_l.setText(QCoreApplication.translate("Config", u":", None))
        self.applyBtn.setText(QCoreApplication.translate("Config", u"\u5e94\u7528", None))
        self.closeBtn.setText(QCoreApplication.translate("Config", u"\u5173\u95ed", None))
        self.AppSettings.setTitle(QCoreApplication.translate("Config", u"\u5e94\u7528\u8bbe\u7f6e", None))
        self.source_l.setText(QCoreApplication.translate("Config", u"\u58c1\u7eb8\u6765\u6e90\uff1a", None))
        self.updateTime_l.setText(QCoreApplication.translate("Config", u"\u66f4\u65b0\u95f4\u9694\uff1a", None))
        self.updateTime.setSuffix(QCoreApplication.translate("Config", u"(\u5206\u949f)", None))
        self.updateTime.setPrefix("")
        self.earthSize_l.setText(QCoreApplication.translate("Config", u"\u5730\u7403\u5927\u5c0f\uff1a", None))
        self.earthSize.setSuffix(QCoreApplication.translate("Config", u"%", None))
        self.wallpaperDir_l.setText(QCoreApplication.translate("Config", u"\u58c1\u7eb8\u6587\u4ef6\u5939\uff1a", None))
        self.selectDir.setText(QCoreApplication.translate("Config", u"\u6d4f\u89c8", None))
        self.wallpaperFile_l.setText(QCoreApplication.translate("Config", u"\u58c1\u7eb8\u6587\u4ef6\uff1a", None))
        self.selectFile.setText(QCoreApplication.translate("Config", u"\u6d4f\u89c8", None))
    # retranslateUi

