import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 加载背景图片
        self.background = QPixmap('hnu.jpg')

        # 创建一个垂直布局
        mainLayout = QVBoxLayout()

        # 创建三个文本框并设置占位符
        self.nameEdit = QLineEdit()
        self.pwdEdit = QLineEdit()
        self.urlEdit = QLineEdit()
        self.nameEdit.setPlaceholderText('Name')
        self.pwdEdit.setPlaceholderText('Password')
        self.urlEdit.setPlaceholderText('URL')

        # 创建一个按钮并连接信号
        btn = QPushButton('提交')
        btn.clicked.connect(self.onSubmit)

        # 对于每个输入框，创建一个水平布局以保持居中
        for label_text, edit_widget in [("用户名", self.nameEdit), 
                                        ("密码", self.pwdEdit), 
                                        ("实训网址", self.urlEdit)]:
            hbox = QHBoxLayout()
            hbox.addStretch()
            vbox_inner = QVBoxLayout()
            vbox_inner.addWidget(QLabel(label_text))
            vbox_inner.addWidget(edit_widget)
            hbox.addLayout(vbox_inner)
            hbox.addStretch()
            mainLayout.addLayout(hbox)

        # 添加按钮到布局
        mainLayout.addWidget(btn, 0, Qt.AlignCenter)

        # 设置窗口的布局
        self.setLayout(mainLayout)
        self.setWindowTitle('')
        self.setGeometry(300, 300, 400, 300)
        self.centerWindow()

        # 应用样式
        self.applyStyles()

    def paintEvent(self, event):
        painter = QPainter(self)

        # 计算背景图片绘制的起始坐标，使其位于窗口中心
        bgWidth = self.background.width()
        bgHeight = self.background.height()
        startX = (self.width() - bgWidth) // 2
        startY = (self.height() - bgHeight) // 2

        painter.drawPixmap(startX, startY, self.background)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def applyStyles(self):
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray;
                border-radius: 10px;
                padding: 5px;
                background: transparent;
            }
            QLineEdit:focus {
                border: 1px solid LightSeaGreen;
            }
        """)

    def onSubmit(self):
        name = self.nameEdit.text()
        pwd = self.pwdEdit.text()
        url = self.urlEdit.text()
        print(f"Name: {name}, Password: {pwd}, URL: {url}")
        
        # 关闭窗口
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())
