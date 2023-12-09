import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QDesktopWidget
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont
import platform
import os
from PyQt5.QtGui import QTextCursor
platf = platform.platform()

class TypewriterEffectApp(QWidget):
    def __init__(self, filepaths):
        super().__init__()
        self.filepaths = filepaths
        self.userIsScrolling = False
        self.initUI()
        self.startTyping()

    def initUI(self):
        layout = QVBoxLayout(self)
        self.textEdit = QTextEdit(self)
        self.textEdit.setReadOnly(True)
        self.textEdit.setFont(QFont('Microsoft YaHei', 16))
        layout.addWidget(self.textEdit)

        self.setWindowSizeAndCenter()

        # 连接滚动条的valueChanged信号
        self.textEdit.verticalScrollBar().valueChanged.connect(self.onScrollBarValueChanged)

    def setWindowSizeAndCenter(self):
        screen = QDesktopWidget().availableGeometry()
        self.resize(int(screen.width() * 0.75), int(screen.height() * 0.75))
        self.centerWindow()

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def startTyping(self):
        self.content = ""
        for filepath in self.filepaths:
            with open(filepath, 'r', encoding='utf-8') as file:
                file_content = file.read()
                # 处理转义字符
                file_content = file_content.replace('\\t', '\t').replace('\\n', '\n')
                self.content += file_content + "\n" + "-" * 50 + "\n"

        self.index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.displayNextCharacter)
        self.timer.start(20)

    def displayNextCharacter(self):
        if self.index < len(self.content):
            char = self.content[self.index]
            text_to_display = self.textEdit.toPlainText() + char

            # 设置光标
            cursor = self.textEdit.textCursor()
            cursor.movePosition(QTextCursor.End)
            cursor.insertText(char)

            # 交替修改光标显示状态
            cursor.clearSelection()
            cursor.setPosition(cursor.position() - 1)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor)
            cursor.setCharFormat(cursor.charFormat())

            self.textEdit.setTextCursor(cursor)

            self.index += 1
            self.textEdit.ensureCursorVisible()  # 始终滚动到底部
        else:
            self.timer.stop()

    def onScrollBarValueChanged(self, value):  # 滚动条滚动时，停止自动滚动
        scroll_bar = self.textEdit.verticalScrollBar()
        self.userIsScrolling = value < scroll_bar.maximum()


def print_txt(json_path: list): # 传入json文件路径
    app = QApplication(sys.argv)
    filepaths = json_path  
    ex = TypewriterEffectApp(filepaths)
    ex.show()
    app.exec_()


def get_all_txt_file(path):
    file_list = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt') and file[0].isdigit():
                file_list.append(os.path.join(root, file))
    file_list.sort(key=lambda x:x.split('.')[0])
    return file_list

if __name__ == '__main__':
    print_txt(get_all_txt_file(os.getcwd()))