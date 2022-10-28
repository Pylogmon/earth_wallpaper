#include "config.h"
#include "ui_config.h"
#include <QDebug>
#include <QDir>
#include <QFile>
#include <QFileDialog>
#include <QMessageBox>
#include <QSettings>
#include <QStandardPaths>

Config::Config(QWidget *parent) : QWidget(parent), ui(new Ui::Config)
{
    this->setAttribute(Qt::WA_DeleteOnClose);
    // 检查配置文件
    this->configPath = QStandardPaths::writableLocation(QStandardPaths::ConfigLocation);

    configPath += "/earth-wallpaper";
    QString path = configPath + "/config";
    QFile configFile = QFile(path);
    QDir configDir = QDir(configPath);
    if (!configFile.exists())
    {
        if (!configDir.exists())
        {
            configDir.mkpath(configPath);
        }
        QString exePath = QCoreApplication::applicationDirPath();
        QFile tempFile = QFile(exePath + "/template/config");
        tempFile.copy(path);
    }
    ui->setupUi(this);
    initUI();
    initConnect();
    readConfig();
    controlOption(ui->earthSource->currentText());
}

Config::~Config()
{
    if (settings) {
        settings->deleteLater();
    }
    this->disconnect();
    delete ui;
}
void Config::initUI()
{
    this->setWindowIcon(QIcon(":/img/cn.huguoyang.earthwallpaper.png"));
    ui->updateTime->addItem("10");
    ui->updateTime->addItem("30");
    ui->updateTime->addItem("60");
    ui->updateTime->addItem("120");
    ui->updateTime->addItem("180");
    ui->updateTime->addItem("720");
    QString exePath = QCoreApplication::applicationDirPath();
    QDir scriptsDir(exePath + "/scripts");
    QStringList nameFilters;
    nameFilters << "*.py";
    scriptsDir.setNameFilters(nameFilters);
    QStringList files = scriptsDir.entryList(QDir::Files, QDir::Name);
    foreach (QString file, files)
    {
        QFile scriptFile(exePath + "/scripts/" + file);
        scriptFile.open(QIODevice::ReadOnly);
        QString info = scriptFile.readLine();
        if (info.split(" ")[1] == "source:")
        {
            ui->earthSource->addItem(info.split(" ")[2].remove("\n"));
        }
    }
}

void Config::initConnect()
{
    connect(ui->apply, &QPushButton::clicked, this, &Config::writeConfig);
    connect(ui->close, &QPushButton::clicked, this, &Config::close);
    connect(ui->earthSource, &QComboBox::currentTextChanged, this, &Config::controlOption);
    connect(ui->select, &QPushButton::clicked, this, &Config::selectDir);
    connect(ui->selectFile, &QPushButton::clicked, this, &Config::selectFile);
}
void Config::readConfig()
{
    if (settings) {
        settings->deleteLater();
    }
    this->settings = new QSettings(configPath + "/config", QSettings::IniFormat);
    settings->setIniCodec("UTF8");

    settings->beginGroup("APP");
    ui->earthSource->setCurrentText(settings->value("earthSource").toString());
    ui->updateTime->setCurrentText(settings->value("updateTime").toString());
    ui->earthSize->setValue(settings->value("earthSize").toInt());
    ui->wallpaperDir->setText(settings->value("wallpaperDir").toString());
    ui->wallpaperFile->setText(settings->value("wallpaperFile").toString());
    settings->endGroup();

    settings->beginGroup("System");
    switch(settings->value("proxy").toInt()){
    case 0:ui->proxyNone->setChecked(true);break;
    case 1:ui->proxyHttp->setChecked(true);break;
    case 2:ui->proxySocks->setChecked(true);break;
    }
    ui->addEdit->setText(settings->value("proxyAdd").toString());
    ui->portEdit->setText(settings->value("proxyPort").toString());
    settings->endGroup();
}
void Config::writeConfig()
{
    settings->setIniCodec("UTF8");

    settings->beginGroup("APP");
    settings->setValue("earthSource", ui->earthSource->currentText());
    settings->setValue("updateTime", ui->updateTime->currentText());
    settings->setValue("earthSize", ui->earthSize->value());
    settings->setValue("wallpaperDir", ui->wallpaperDir->text());
    settings->setValue("wallpaperFile", ui->wallpaperFile->text());
    settings->endGroup();

    settings->beginGroup("System");
    if(ui->proxyNone->isChecked()){
        settings->setValue("proxy",0);
    }else if(ui->proxyHttp->isChecked()){
        settings->setValue("proxy",1);
    }else if(ui->proxySocks->isChecked()){
        settings->setValue("proxy",2);
    }
    settings->setValue("proxyAdd",ui->addEdit->text());
    settings->setValue("proxyPort",ui->portEdit->text());
    settings->endGroup();

    QMessageBox::information(this, tr("设置"), tr("设置保存成功！"));
    emit configChanged();
}
void Config::controlOption(QString source)
{
    QString exePath = QCoreApplication::applicationDirPath();
    QDir scriptsDir(exePath + "/scripts");
    QStringList nameFilters;
    nameFilters << "*.py";
    scriptsDir.setNameFilters(nameFilters);
    QStringList files = scriptsDir.entryList(QDir::Files, QDir::Name);
    foreach (QString file, files)
    {
        QFile scriptFile(exePath + "/scripts/" + file);
        scriptFile.open(QIODevice::ReadOnly);
        QString info = scriptFile.readLine();
        if (info.split(" ")[1] == "source:")
        {
            if (info.split(" ")[2].remove("\n") == source)
            {
                QString itemInfo = scriptFile.readLine();
                if (itemInfo.contains("updateTime"))
                {
                    ui->label_2->show();
                    ui->updateTime->show();
                }
                else
                {
                    settings->setValue("APP/updateTime", "10");
                    ui->label_2->hide();
                    ui->updateTime->hide();
                }
                if (itemInfo.contains("earthSize"))
                {
                    ui->label_3->show();
                    ui->earthSize->show();
                }
                else
                {
                    ui->label_3->hide();
                    ui->earthSize->hide();
                }
                if (itemInfo.contains("wallpaperDir"))
                {
                    ui->label_4->show();
                    ui->wallpaperDir->show();
                    ui->select->show();
                }
                else
                {
                    ui->label_4->hide();
                    ui->wallpaperDir->hide();
                    ui->select->hide();
                }
                if (itemInfo.contains("wallpaperFile"))
                {
                    ui->label_5->show();
                    ui->wallpaperFile->show();
                    ui->selectFile->show();
                }
                else
                {
                    ui->label_5->hide();
                    ui->wallpaperFile->hide();
                    ui->selectFile->hide();
                }
            }
        }
    }
}
void Config::selectDir()
{
    QString dir = QFileDialog::getExistingDirectory(this, tr("选择壁纸文件夹"));
    ui->wallpaperDir->setText(dir);
}
void Config::selectFile()
{
    QString file =
        QFileDialog::getOpenFileName(this, "选择24h壁纸文件", "", "24h壁纸文件 (*.ddw *.zip);; 所有文件 (*.*);; ");
    ui->wallpaperFile->setText(file);
}

void Config::closeEvent(QCloseEvent *event)
{
    emit closed();
}
