#include "trayicon.h"
#include "config.h"
#include <qaction.h>

TrayIcon::TrayIcon(QSystemTrayIcon *parent)
{
    initTrayIcon();
    initConnect();
}
TrayIcon::~TrayIcon()
{
    config->deleteLater();
    exit->deleteLater();
    trayIconMenu->deleteLater();
}
void TrayIcon::initConnect()
{
    connect(this->exit, &QAction::triggered, this, &TrayIcon::OnExit);
    connect(this->config, &QAction::triggered, this, &TrayIcon::showConfigPage);
}
void TrayIcon::initTrayIcon()
{
    this->setIcon(QIcon(":/img/icon.png"));

    trayIconMenu = new QMenu();
    config = new QAction();
    exit = new QAction();
    config->setText("设置");
    exit->setText("退出");

    trayIconMenu->addAction(config);
    trayIconMenu->addAction(exit);

    this->setContextMenu(trayIconMenu);

    this->show();
}

void TrayIcon::OnExit()
{
    qApp->exit(0);
}

void TrayIcon::showConfigPage()
{
    auto config = new Config;
    config->show();
}
