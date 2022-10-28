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
  signals:
    void configChanged();
    void closed();

  public:
    QString configPath;
    QSettings *settings = nullptr;
    explicit Config(QWidget *parent = nullptr);
    ~Config() override;

    void initUI();
    void initConnect();
    void readConfig();
    void writeConfig();
    void controlOption(QString source);
    void selectDir();
    void selectFile();

    void closeEvent(QCloseEvent *event) override;

  private:
    Ui::Config *ui;
};
