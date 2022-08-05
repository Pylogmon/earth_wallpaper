#include "trayicon.h"
#include <QApplication>
#include <QMessageBox>
#include <QSharedMemory>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    QApplication::setQuitOnLastWindowClosed(false); // 最后一个窗口关闭时，禁止退出应用程序
    QSharedMemory shared("earth-wallpaper");

    // 防止重复运行
    if (shared.attach())
    {
        QMessageBox::information(nullptr, "警告", "程序已经运行", QMessageBox::Yes);
        return EXIT_SUCCESS;
    }
    shared.create(1);

    TrayIcon tray;
    return QApplication::exec();
}
