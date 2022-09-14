#pragma once

#include <QThread>

class Thread : public QThread
{
  public:
    QStringList command;
    explicit Thread(QStringList command);
    ~Thread() override;

    void run() override;
};
