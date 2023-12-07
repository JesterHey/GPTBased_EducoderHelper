'''
本模块用于创建登录界面并保存用户信息
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt,QTimer
from PyQt5.QtGui import QPixmap, QPainter
import os
import platform
import json

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 加载背景图片
        self.background = QPixmap()
        # 创建一个垂直布局
        mainLayout = QVBoxLayout()

        # 创建三个文本框并设置占位符
        self.nameEdit = QLineEdit()
        self.pwdEdit = QLineEdit()
        self.urlEdit = QLineEdit()

        # 创建一个按钮并连接信号
        btn = QPushButton('提交')
        btn.clicked.connect(self.onSubmit)

        # 创建一个用于显示错误信息的标签
        self.errorLabel = QLabel('', self)
        self.errorLabel.hide()  # 初始时隐藏该标签

        self.setWindowTitle('头歌助手登录')

        # 对于每个输入框，创建一个水平布局以保持居中
        for label_text, edit_widget in [("用户名", self.nameEdit), 
                                        ("密   码", self.pwdEdit), 
                                        ("实训网址", self.urlEdit)]:
            hbox = QHBoxLayout()
            hbox.addStretch()
            vbox_inner = QVBoxLayout()
            vbox_inner.addWidget(QLabel(label_text))
            vbox_inner.addWidget(edit_widget)
            hbox.addLayout(vbox_inner)
            hbox.addStretch()
            mainLayout.addLayout(hbox)

        # 添加按钮和错误信息标签到布局
        mainLayout.addWidget(btn, 0, Qt.AlignCenter)
        mainLayout.addWidget(self.errorLabel, 0, Qt.AlignCenter)

        # 设置窗口的布局
        self.setLayout(mainLayout)
        self.setGeometry(300, 300, 650, 550)
        self.centerWindow()

        # 应用样式
        self.applyStyles()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background)

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
                background: rgba(255, 255, 255, 100);  
                color: black;
                width: 300px;
                height: 30px;
            }
            QLineEdit:focus {
                border: 3px solid black;
            }
            QLabel {
                color: black;
                font-size: 20pt;
                font-family: "Microsoft YaHei";
            }
            QPushButton {
                border: 1px solid gray;
                border-radius: 10px;
                background: rgba(255, 255, 255, 100);
                color: black;
                width: 100px;
                height: 27px;
            }
            /* 样式用于错误信息标签 */
            QLabel#errorLabel {
                color: red;
                font-size: 16pt;
            }
        """)

    def onSubmit(self):
        name = self.nameEdit.text()
        pwd = self.pwdEdit.text()
        url = self.urlEdit.text()
        
        if name == '' or pwd == '' or url == '':
            self.showError("非法输入！")
        else:
            with open('userinfo.json', 'w') as f:
                json.dump({'name': name, 'pwd': pwd, 'url': url}, f)
            self.close()

    def showError(self, message):
        self.errorLabel.setText(message)
        self.errorLabel.show()
        QTimer.singleShot(2000, self.hideError)

    def hideError(self):
        self.errorLabel.hide()

def main():
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
