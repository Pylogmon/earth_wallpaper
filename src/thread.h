#pragma once

#include <QThread>

class Thread : public QThread
{
  public:
    QString command;
    explicit Thread(QString command);
    ~Thread() override;

    void run() override;
};
