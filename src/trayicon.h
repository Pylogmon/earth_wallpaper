#pragma once

#include "config.h"
#include <QApplication>
#include <QMenu>
#include <QSettings>
#include <QSystemTrayIcon>
#include <QTimer>
#include <qaction.h>

class TrayIcon : public QSystemTrayIcon
{
    Q_OBJECT
  public:
    QTimer timer;
    int height;
    int width;
    QSettings *settings = nullptr;
    Config *configPage;
    QMenu *trayIconMenu;
    QAction *config;
    QAction *exit;
    QAction *refresh;
    QAction *save;
    explicit TrayIcon(QSystemTrayIcon *parent = nullptr);
    ~TrayIcon() override;

    void initTrayIcon();   //初始化托盘图标
    void initConnect();    //初始化信号槽
    void OnExit();         //退出程序
    void showConfigPage(); //显示配置界面
    void checkConfig();    //检查配置文件
    void reloadSettings(); //启动线程
    void handle();
    void saveCurrentImg();
};
