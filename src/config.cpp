#include "config.h"
#include "ui_config.h"
#include <QDebug>
#include <QDir>
#include <QFile>
#include <QMessageBox>
#include <QSettings>
#include <QStandardPaths>

Config::Config(QWidget *parent) : QWidget(parent), ui(new Ui::Config)
{
    this->setAttribute(Qt::WA_DeleteOnClose);
    //检查配置文件
    this->configPath = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);
    configPath += "/earth_wallpaper/config_user";
    QString path = configPath;
    auto configFile = new QFile(path);
    if (!configFile->exists())
    {
        path = path.remove("_user");
        auto tempFile = QFile(path);
        if (!tempFile.exists())
        {
            qFatal("配置文件缺失！");
        }
        else
        {
            qInfo("用户配置不存在，创建配置文件");
            path += "_user";
            tempFile.copy(path);
        }
    }
    ui->setupUi(this);
    initUI();
    initConnect();
    readConfig();
}

Config::~Config()
{
    settings->deleteLater();
    this->disconnect();
    delete ui;
}
void Config::initUI()
{
    this->setWindowIcon(QIcon(":/img/icon.png"));
    ui->earthSource->addItem("向日葵八号");
    ui->earthSource->addItem("风云四号");
    ui->updateTime->addItem("10");
    ui->updateTime->addItem("30");
    ui->updateTime->addItem("60");
    ui->updateTime->addItem("120");
    ui->updateTime->addItem("180");
}
void Config::initConnect()
{
    connect(ui->apply, &QPushButton::clicked, this, &Config::writeConfig);
    connect(ui->close, &QPushButton::clicked, this, &Config::close);
}
void Config::readConfig()
{
    this->settings = new QSettings(configPath, QSettings::IniFormat);
    settings->setIniCodec("UTF8");
    settings->beginGroup("APP");
    ui->earthSource->setCurrentIndex(settings->value("earthSource").toInt());
    ui->updateTime->setCurrentText(settings->value("updateTime").toString());
    ui->alwaysUpdate->setChecked(settings->value("alwaysUpdate").toBool());
    settings->endGroup();
    settings->beginGroup("System");
    ui->startWithSystem->setChecked(settings->value("startWithSystem").toBool());
    settings->endGroup();
}
void Config::writeConfig()
{
    settings->beginGroup("APP");
    settings->setValue("earthSource", ui->earthSource->currentIndex());
    settings->setValue("updateTime", ui->updateTime->currentText());
    settings->setValue("alwaysUpdate", ui->alwaysUpdate->isChecked());
    settings->endGroup();
    settings->beginGroup("System");
    settings->setValue("startWithSystem", ui->startWithSystem->isChecked());
    settings->endGroup();
    QMessageBox::information(this, tr("设置"), tr("设置保存成功！"));
    emit configChanged();
}