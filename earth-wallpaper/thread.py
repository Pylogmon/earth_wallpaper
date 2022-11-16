from PySide6.QtCore import QThread, QTimer
from PySide6.QtWidgets import QMessageBox
import interfaces


def get_class_name(name: str):
    for i in dir(interfaces):
        if getattr(interfaces, i).name() == name:
            return i


class Thread(QThread):

    def __init__(self, name):
        super(Thread, self).__init__()
        self.class_name = get_class_name(name)
        self.timer=QTimer()
        self.timer.start(30000)
        self.timer.timeout.connect(self.on_timeout)

    def run(self):
        x = getattr(interfaces, self.class_name)()
        print(f"Start run {x.name()}...")
        x.run()
        self.timer.stop()
        print("Run completed!")
    
    def on_timeout(self):
        message = QMessageBox()
        QMessageBox.warning(message, "超时!", "子线程处理超时,已自动关闭,请检查网络后重试!", QMessageBox.Yes)
        self.terminate()
