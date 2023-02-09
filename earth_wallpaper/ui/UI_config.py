# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'config.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QSpacerItem,
    QSpinBox, QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(376, 737)
        self.gridLayout_3 = QGridLayout(Config)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.AppSettings = QGroupBox(Config)
        self.AppSettings.setObjectName(u"AppSettings")
        self.gridLayout_2 = QGridLayout(self.AppSettings)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.source_l = QLabel(self.AppSettings)
        self.source_l.setObjectName(u"source_l")

        self.gridLayout_2.addWidget(self.source_l, 0, 0, 1, 1)

        self.source = QComboBox(self.AppSettings)
        self.source.setObjectName(u"source")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.source.sizePolicy().hasHeightForWidth())
        self.source.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.source, 0, 1, 1, 3)

        self.updateTime_l = QLabel(self.AppSettings)
        self.updateTime_l.setObjectName(u"updateTime_l")

        self.gridLayout_2.addWidget(self.updateTime_l, 1, 0, 1, 1)

        self.updateTime = QSpinBox(self.AppSettings)
        self.updateTime.setObjectName(u"updateTime")
        sizePolicy.setHeightForWidth(self.updateTime.sizePolicy().hasHeightForWidth())
        self.updateTime.setSizePolicy(sizePolicy)
        self.updateTime.setMinimum(1)
        self.updateTime.setMaximum(1440)
        self.updateTime.setValue(30)

        self.gridLayout_2.addWidget(self.updateTime, 1, 1, 1, 3)

        self.earthSize_l = QLabel(self.AppSettings)
        self.earthSize_l.setObjectName(u"earthSize_l")

        self.gridLayout_2.addWidget(self.earthSize_l, 2, 0, 1, 1)

        self.earthSize = QSpinBox(self.AppSettings)
        self.earthSize.setObjectName(u"earthSize")
        sizePolicy.setHeightForWidth(self.earthSize.sizePolicy().hasHeightForWidth())
        self.earthSize.setSizePolicy(sizePolicy)
        self.earthSize.setMinimum(20)
        self.earthSize.setMaximum(100)

        self.gridLayout_2.addWidget(self.earthSize, 2, 2, 1, 2)

        self.wallpaperDir_l = QLabel(self.AppSettings)
        self.wallpaperDir_l.setObjectName(u"wallpaperDir_l")

        self.gridLayout_2.addWidget(self.wallpaperDir_l, 3, 0, 1, 2)

        self.wallpaperDir = QLineEdit(self.AppSettings)
        self.wallpaperDir.setObjectName(u"wallpaperDir")

        self.gridLayout_2.addWidget(self.wallpaperDir, 3, 2, 1, 1)

        self.selectDir = QPushButton(self.AppSettings)
        self.selectDir.setObjectName(u"selectDir")
        self.selectDir.setMinimumSize(QSize(80, 0))

        self.gridLayout_2.addWidget(self.selectDir, 3, 3, 1, 1)

        self.wallpaperFile_l = QLabel(self.AppSettings)
        self.wallpaperFile_l.setObjectName(u"wallpaperFile_l")

        self.gridLayout_2.addWidget(self.wallpaperFile_l, 4, 0, 1, 1)

        self.wallpaperFile = QLineEdit(self.AppSettings)
        self.wallpaperFile.setObjectName(u"wallpaperFile")

        self.gridLayout_2.addWidget(self.wallpaperFile, 4, 2, 1, 1)

        self.selectFile = QPushButton(self.AppSettings)
        self.selectFile.setObjectName(u"selectFile")
        self.selectFile.setMinimumSize(QSize(80, 0))

        self.gridLayout_2.addWidget(self.selectFile, 4, 3, 1, 1)

        self.apikey_l = QLabel(self.AppSettings)
        self.apikey_l.setObjectName(u"apikey_l")

        self.gridLayout_2.addWidget(self.apikey_l, 5, 0, 1, 1)

        self.apikey = QLineEdit(self.AppSettings)
        self.apikey.setObjectName(u"apikey")

        self.gridLayout_2.addWidget(self.apikey, 5, 1, 1, 3)

        self.searchkey_l = QLabel(self.AppSettings)
        self.searchkey_l.setObjectName(u"searchkey_l")

        self.gridLayout_2.addWidget(self.searchkey_l, 6, 0, 1, 1)

        self.searchkey = QLineEdit(self.AppSettings)
        self.searchkey.setObjectName(u"searchkey")

        self.gridLayout_2.addWidget(self.searchkey, 6, 1, 1, 3)

        self.categoriesGroup = QHBoxLayout()
        self.categoriesGroup.setObjectName(u"categoriesGroup")
        self.categories_l = QLabel(self.AppSettings)
        self.categories_l.setObjectName(u"categories_l")

        self.categoriesGroup.addWidget(self.categories_l)

        self.General = QCheckBox(self.AppSettings)
        self.General.setObjectName(u"General")

        self.categoriesGroup.addWidget(self.General)

        self.Anime = QCheckBox(self.AppSettings)
        self.Anime.setObjectName(u"Anime")

        self.categoriesGroup.addWidget(self.Anime)

        self.People = QCheckBox(self.AppSettings)
        self.People.setObjectName(u"People")

        self.categoriesGroup.addWidget(self.People)


        self.gridLayout_2.addLayout(self.categoriesGroup, 7, 0, 1, 4)

        self.purityGroup = QHBoxLayout()
        self.purityGroup.setObjectName(u"purityGroup")
        self.purity_l = QLabel(self.AppSettings)
        self.purity_l.setObjectName(u"purity_l")

        self.purityGroup.addWidget(self.purity_l)

        self.SFW = QCheckBox(self.AppSettings)
        self.SFW.setObjectName(u"SFW")
        self.SFW.setStyleSheet(u"font: 700;\n"
"color: #447744;")

        self.purityGroup.addWidget(self.SFW)

        self.Sketchy = QCheckBox(self.AppSettings)
        self.Sketchy.setObjectName(u"Sketchy")
        self.Sketchy.setStyleSheet(u"font: 700;\n"
"color: #777744;")

        self.purityGroup.addWidget(self.Sketchy)

        self.NSFW = QCheckBox(self.AppSettings)
        self.NSFW.setObjectName(u"NSFW")
        self.NSFW.setStyleSheet(u"font: 700;\n"
"color: #774444;")

        self.purityGroup.addWidget(self.NSFW)


        self.gridLayout_2.addLayout(self.purityGroup, 8, 0, 1, 4)

        self.sorting_l = QLabel(self.AppSettings)
        self.sorting_l.setObjectName(u"sorting_l")

        self.gridLayout_2.addWidget(self.sorting_l, 9, 0, 1, 1)

        self.sorting = QComboBox(self.AppSettings)
        self.sorting.setObjectName(u"sorting")
        sizePolicy.setHeightForWidth(self.sorting.sizePolicy().hasHeightForWidth())
        self.sorting.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.sorting, 9, 1, 1, 3)

        self.color_l = QLabel(self.AppSettings)
        self.color_l.setObjectName(u"color_l")

        self.gridLayout_2.addWidget(self.color_l, 10, 0, 1, 1)

        self.color = QComboBox(self.AppSettings)
        self.color.setObjectName(u"color")
        sizePolicy.setHeightForWidth(self.color.sizePolicy().hasHeightForWidth())
        self.color.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.color, 10, 1, 1, 3)

        self.atleast_l = QLabel(self.AppSettings)
        self.atleast_l.setObjectName(u"atleast_l")

        self.gridLayout_2.addWidget(self.atleast_l, 11, 0, 1, 1)

        self.atleast = QComboBox(self.AppSettings)
        self.atleast.setObjectName(u"atleast")

        self.gridLayout_2.addWidget(self.atleast, 11, 1, 1, 3)


        self.gridLayout_3.addWidget(self.AppSettings, 0, 0, 1, 3)

        self.SystemSettings = QGroupBox(Config)
        self.SystemSettings.setObjectName(u"SystemSettings")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.SystemSettings.sizePolicy().hasHeightForWidth())
        self.SystemSettings.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.SystemSettings)
        self.gridLayout.setObjectName(u"gridLayout")
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


        self.gridLayout.addLayout(self.proxyTypeGroup, 0, 0, 1, 2)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.portEdit.sizePolicy().hasHeightForWidth())
        self.portEdit.setSizePolicy(sizePolicy2)
        self.portEdit.setMinimumSize(QSize(20, 0))

        self.addGroup.addWidget(self.portEdit)


        self.gridLayout.addLayout(self.addGroup, 1, 0, 1, 2)

        self.clearCache = QPushButton(self.SystemSettings)
        self.clearCache.setObjectName(u"clearCache")

        self.gridLayout.addWidget(self.clearCache, 2, 0, 1, 2)

        self.scripts_l = QLabel(self.SystemSettings)
        self.scripts_l.setObjectName(u"scripts_l")

        self.gridLayout.addWidget(self.scripts_l, 3, 0, 1, 1)

        self.scripts = QLineEdit(self.SystemSettings)
        self.scripts.setObjectName(u"scripts")

        self.gridLayout.addWidget(self.scripts, 3, 1, 1, 1)


        self.gridLayout_3.addWidget(self.SystemSettings, 1, 0, 1, 3)

        self.applySpacer = QSpacerItem(57, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.applySpacer, 2, 0, 1, 1)

        self.applyBtn = QPushButton(Config)
        self.applyBtn.setObjectName(u"applyBtn")

        self.gridLayout_3.addWidget(self.applyBtn, 2, 1, 1, 1)

        self.closeBtn = QPushButton(Config)
        self.closeBtn.setObjectName(u"closeBtn")

        self.gridLayout_3.addWidget(self.closeBtn, 2, 2, 1, 1)


        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"\u8bbe\u7f6e", None))
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
        self.apikey_l.setText(QCoreApplication.translate("Config", u"apiKey\uff1a", None))
        self.apikey.setInputMask("")
        self.apikey.setText("")
        self.apikey.setPlaceholderText(QCoreApplication.translate("Config", u"\u4f7f\u7528NSFW\u9700\u8981\u63d0\u4f9bapikey", None))
        self.searchkey_l.setText(QCoreApplication.translate("Config", u"\u5173\u952e\u8bcd\uff1a", None))
        self.categories_l.setText(QCoreApplication.translate("Config", u"\u5206\u7c7b\uff1a", None))
        self.General.setText(QCoreApplication.translate("Config", u"General", None))
        self.Anime.setText(QCoreApplication.translate("Config", u"Anime", None))
        self.People.setText(QCoreApplication.translate("Config", u"People", None))
        self.purity_l.setText(QCoreApplication.translate("Config", u"\u5206\u7ea7\uff1a", None))
        self.SFW.setText(QCoreApplication.translate("Config", u"SFW", None))
        self.Sketchy.setText(QCoreApplication.translate("Config", u"Sketchy", None))
        self.NSFW.setText(QCoreApplication.translate("Config", u"NSFW", None))
        self.sorting_l.setText(QCoreApplication.translate("Config", u"\u968f\u673a\u5217\u8868\uff1a", None))
        self.color_l.setText(QCoreApplication.translate("Config", u"\u989c\u8272\uff1a", None))
        self.atleast_l.setText(QCoreApplication.translate("Config", u"\u6700\u5c0f\u5c3a\u5bf8\uff1a", None))
        self.SystemSettings.setTitle(QCoreApplication.translate("Config", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.proxy_l.setText(QCoreApplication.translate("Config", u"\u7f51\u7edc\u4ee3\u7406\uff1a", None))
        self.proxyNone.setText(QCoreApplication.translate("Config", u"\u65e0", None))
        self.proxyHttp.setText(QCoreApplication.translate("Config", u"http", None))
        self.proxySocks.setText(QCoreApplication.translate("Config", u"socks", None))
        self.add_l.setText(QCoreApplication.translate("Config", u"\u5730\u5740\uff1a", None))
        self.port_l.setText(QCoreApplication.translate("Config", u":", None))
        self.clearCache.setText(QCoreApplication.translate("Config", u"\u5220\u9664\u7f13\u5b58", None))
        self.scripts_l.setText(QCoreApplication.translate("Config", u"\u5916\u90e8\u811a\u672c\uff1a", None))
        self.scripts.setPlaceholderText(QCoreApplication.translate("Config", u"\u6b63\u5e38\u4f7f\u7528\u4e0d\u9700\u8981\u586b\u5199\uff0c\u7528\u6765\u8bbe\u7f6e\u58c1\u7eb8\u7684\u811a\u672c", None))
        self.applyBtn.setText(QCoreApplication.translate("Config", u"\u5e94\u7528", None))
        self.closeBtn.setText(QCoreApplication.translate("Config", u"\u5173\u95ed", None))
    # retranslateUi

