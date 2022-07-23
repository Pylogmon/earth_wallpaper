#pragma once

#include <QApplication>
#include <QMenu>
#include <QSystemTrayIcon>

class TrayIcon : public QSystemTrayIcon
{
    Q_OBJECT
  signals:
    void updateTrayIconSignal();

  public:
    QMenu *trayIconMenu;
    QAction *config;
    QAction *exit;
    explicit TrayIcon(QSystemTrayIcon *parent = nullptr);
    ~TrayIcon() override;

    void initTrayIcon();   //初始化托盘图标
    void initConnect();    //初始化信号槽
    void OnExit();         //退出程序
    void showConfigPage(); //显示配置界面
};
