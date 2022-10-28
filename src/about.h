#pragma once

#include <QWidget>

#define VERSION "1.8.6"

QT_BEGIN_NAMESPACE
namespace Ui
{
class About;
}
QT_END_NAMESPACE

class About : public QWidget
{
    Q_OBJECT

  signals:
    void closed();

  public:
    explicit About(QWidget *parent = nullptr);
    ~About() override;

    void initUI();
    void initConnect();
    void checkUpdate();

    void closeEvent(QCloseEvent *event) override;

  private:
    Ui::About *ui;
};
