import sys
from PyQt5.QtWidgets import QApplication, QLabel, QWidget, QDesktopWidget
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

        # 获取屏幕尺寸
        screen = QDesktopWidget().screenGeometry()

        # 缩放图片大小
        # 过时警告 scaled_pixmap = pixmap.scaledint(screen.width() * 0.5, screen.height() * 0.5, Qt.KeepAspectRatio)
        scaled_pixmap = pixmap.scaled(int(screen.width() * 0.5), int(screen.height() * 0.5), Qt.KeepAspectRatio)
        label.setPixmap(scaled_pixmap)
        self.resize(scaled_pixmap.width(), scaled_pixmap.height())

        # 居中显示窗口
        self.centerWindow()

        QTimer.singleShot(4500, self.close)

    def centerWindow(self):
        # 居中窗口
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center() # 获取屏幕中心点
        qr.moveCenter(cp)
        self.move(qr.topLeft())

def show_image():
    app = QApplication(sys.argv)
    ex = ImageWindow('picture\\b2txt.png')  # 图片路径
    ex.show()
    sys.exit(app.exec_())


show_image()