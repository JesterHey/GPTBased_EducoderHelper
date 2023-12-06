import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, Qt

class ImageWindow(QWidget):
    def __init__(self, image_path):
        super().__init__()
        self.initUI(image_path)

    def initUI(self, image_path):
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        label = QLabel(self)
        pixmap = QPixmap(image_path)

        # 缩放图片到期望的大小
        scaled_pixmap = pixmap.scaled(700, 400, Qt.KeepAspectRatio)  # 设置图片大小为400x300，并保持纵横比
        label.setPixmap(scaled_pixmap)
        self.resize(scaled_pixmap.width(), scaled_pixmap.height())

        # 居中显示窗口
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

        QTimer.singleShot(3000, self.close)

def show():
    app = QApplication(sys.argv)
    ex = ImageWindow('b2.png')
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    show()

