import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter
import os
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 加载背景图片
        self.background = QPixmap('b3o.png')
        # 创建一个垂直布局
        mainLayout = QVBoxLayout()

        # 创建三个文本框并设置占位符
        self.nameEdit = QLineEdit()
        self.pwdEdit = QLineEdit()
        self.urlEdit = QLineEdit()
        # self.nameEdit.setPlaceholderText('Name')
        # self.pwdEdit.setPlaceholderText('Password')
        # self.urlEdit.setPlaceholderText('URL')

        # 创建一个按钮并连接信号
        btn = QPushButton('提交')
        btn.clicked.connect(self.onSubmit)

        self.setWindowTitle('头歌助手登录')
        # 对于每个输入框，创建一个水平布局以保持居中
        for label_text, edit_widget in [("用户名", self.nameEdit), 
                                        ("密    码", self.pwdEdit), 
                                        ("实训网址", self.urlEdit)]:
            hbox = QHBoxLayout() #创建一个水平布局
            hbox.addStretch() #添加一个伸缩因子，使得文本框和按钮位于窗口中心
            vbox_inner = QVBoxLayout() #创建一个垂直布局
            vbox_inner.addWidget(QLabel(label_text)) #添加一个标签
            vbox_inner.addWidget(edit_widget) #添加一个文本框
            hbox.addLayout(vbox_inner) #将垂直布局添加到水平布局中
            hbox.addStretch() #添加一个伸缩因子，使得文本框和按钮位于窗口中心
            mainLayout.addLayout(hbox) #将水平布局添加到垂直布局中

        # 添加按钮到布局
        mainLayout.addWidget(btn, 0, Qt.AlignCenter)

        # 设置窗口的布局
        self.setLayout(mainLayout)
        self.setWindowTitle('')
        self.setGeometry(300, 300, 650,550) # 设置窗口大小,其中300,300为窗口左上角坐标，1000,600为窗口大小
        self.centerWindow()

        # 应用样式
        self.applyStyles()
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawPixmap(self.rect(), self.background)

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def applyStyles(self):
        # css 用于设置窗口样式
        self.setStyleSheet("""
            QLineEdit {
                border: 1px solid gray; 
                border-radius: 10px; 
                padding: 5px; 
                background: rgba(255, 255, 255, 100);  
            }
            QLineEdit:focus {
                border: 1px solid black;
            }
            QLabel {
            color: black;
            font-size: 23pt;
            margin-top: 50px; /* 顶部外边距 */
            margin-left: 20px; /* 左侧外边距 */
        }
            QLineEdit {
            border: 1px solid gray;
            border-radius: 10px;
            padding: 5px;
            background: rgba(255, 255, 255, 100);
            color: black; /* 设置输入文本颜色为黑色 */
            width: 300px; /* 设置输入框宽度 */
            height: 30px; /* 设置输入框高度 */
        }
            QPushButton {
            border: 1px solid gray;
            border-radius: 10px;
            padding: 5px;
            background: rgba(255, 255, 255, 100);
            color: black; /* 设置按钮文本颜色为黑色 */
            width: 100px; /* 设置按钮宽度 */
            height: 27px; /* 设置按钮高度 */
        }
        """)

    def onSubmit(self):
        name = self.nameEdit.text()
        pwd = self.pwdEdit.text()
        url = self.urlEdit.text()
        print(f"Name: {name}, Password: {pwd}, URL: {url}")
        
        # 关闭窗口
        self.close()
os.system('python3 show_welcome.py')
app = QApplication(sys.argv)
ex = MyApp()
ex.show()
sys.exit(app.exec_())