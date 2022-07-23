#pragma once

#include <QSettings>
#include <QWidget>

QT_BEGIN_NAMESPACE
namespace Ui
{
class Config;
}
QT_END_NAMESPACE

class Config : public QWidget
{
    Q_OBJECT

  public:
    QString configPath;
    QSettings *settings;
    Config(QWidget *parent = nullptr);
    ~Config();

    void initUI();
    void initConnect();
    void readConfig();
    void writeConfig();

  private:
    Ui::Config *ui;
};
