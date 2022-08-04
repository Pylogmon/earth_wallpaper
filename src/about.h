#pragma once

#include <QWidget>

#define VERSION "1.3.0.r5.g28c8bf6"

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
    explicit About(QWidget *parent = nullptr);
    ~About() override;

    void initUI();
    void initConnect();

  private:
    Ui::About *ui;
};
