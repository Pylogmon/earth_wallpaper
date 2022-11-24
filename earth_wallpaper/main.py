#!/bin/python3
import sys
import os

# 添加path路径，否则有可能会找不到模块
sys.path.append(os.path.abspath(os.path.dirname(os.path.dirname(__file__))))
from PySide2.QtWidgets import QApplication
from earth_wallpaper.systemtray import SystemTray
from earth_wallpaper.about import check_update
from earth_wallpaper.utils.platformInfo import PlatformInfo
import logging


# from PySide2.QtCore import QSharedMemory


def main():
    app = QApplication()

    QApplication.setQuitOnLastWindowClosed(False)

    # 初始化日志系统
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s %(levelname)s: [%(filename)s](%(funcName)s) -> %(message)s',
                                  datefmt='%H:%M:%S')
    # 输出到文件
    fh = logging.FileHandler(PlatformInfo.log_path())
    fh.setFormatter(formatter)

    # 输出到控制台
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)

    logger.addHandler(ch)
    logger.addHandler(fh)

    logger.info('日志系统启动')

    tray = SystemTray()
    check_update()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
