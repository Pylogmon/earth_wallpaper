#pragma once

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
    Config(QWidget *parent = nullptr);
    ~Config();

  private:
    Ui::Config *ui;
};
