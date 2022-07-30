#pragma once

#include <QWidget>

#define VERSION "1.3.0"

QT_BEGIN_NAMESPACE
namespace Ui
{
class About;
}
QT_END_NAMESPACE

class About : public QWidget
{
    Q_OBJECT
  public:
    About(QWidget *parent = nullptr);
    ~About();

    void initUI();
    void initConnect();

  private:
    Ui::About *ui;
};
