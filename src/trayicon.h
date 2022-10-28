#pragma once

#include "about.h"
#include "config.h"
#include "thread.h"
#include <QApplication>
#include <QMenu>
#include <QSettings>
#include <QSystemTrayIcon>
#include <QTimer>

class TrayIcon : public QSystemTrayIcon
{
    Q_OBJECT
  public:
    int height;
    int width;
    QTimer timer;
    Thread *thread = nullptr;
    QSettings *settings = nullptr;
    Config *configPage = nullptr;
    About *aboutPage = nullptr;
    QMenu *trayIconMenu = nullptr;
    QAction *config = nullptr;
    QAction *exit = nullptr;
    QAction *refresh = nullptr;
    QAction *save = nullptr;
    QAction *about = nullptr;

    explicit TrayIcon(QSystemTrayIcon *parent = nullptr);
    ~TrayIcon() override;

    void initTrayIcon();   // 初始化托盘图标
    void initConnect();    // 初始化信号槽
    static void OnExit();  // 退出程序
    void showConfigPage(); // 显示配置界面
    void showAboutPage();
    void checkConfig();    // 检查配置文件
    void reloadSettings(); // 启动线程
    void handle();
    static void saveCurrentImg();
};
