#include "trayicon.h"
#include "config.h"
#include <QDebug>
#include <QFile>
#include <QStandardPaths>
#include <qnumeric.h>
#include <qstandardpaths.h>

TrayIcon::TrayIcon(QSystemTrayIcon *parent)
{
    initTrayIcon();
    initConnect();
    checkConfig();
}
TrayIcon::~TrayIcon()
{
    config->deleteLater();
    exit->deleteLater();
    trayIconMenu->deleteLater();
    thread->deleteLater();
}
void TrayIcon::initConnect()
{
    //退出程序
    connect(this->exit, &QAction::triggered, this, &TrayIcon::OnExit);
    //打开设置页面
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
    this->configPage = new Config;
    configPage->show();
    //重启线程
    connect(this->configPage, &Config::configChanged, this, &TrayIcon::restartThread);
}

void TrayIcon::checkConfig()
{
    QString path = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    path += "/earth_wallpaper/config_user";
    auto configFile = QFile(path);
    if (!configFile.exists())
    {
        qInfo() << "首次运行，打开设置页面";
        this->showConfigPage();
    }
    else
    {
        restartThread();
    }
}

void TrayIcon::restartThread()
{
    if (this->thread != nullptr)
    {
        thread->deleteLater();
    }
    QString configPath = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    configPath += "/earth_wallpaper/config_user";
    if (settings != nullptr)
    {
        delete settings;
    }
    //重新读取配置文件
    this->settings = new QSettings(configPath, QSettings::IniFormat);
    thread = new Thread(settings);
    thread->start();
}