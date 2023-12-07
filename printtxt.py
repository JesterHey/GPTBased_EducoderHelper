import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QDesktopWidget, QScrollBar
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QFont

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
            with open(filepath, 'r') as file:
                self.content += file.read() + "\n" + "-"*50 + "\n"

        self.index = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.displayNextCharacter)
        self.timer.start(5)

    def displayNextCharacter(self):
        if self.index < len(self.content):
            char = self.content[self.index]
            #如果char和下一个字符是\n，那么就要执行换行
            if char == '\n' and self.content[self.index+1] == '\n':
                text_to_display = self.textEdit.toPlainText() + '\n\n'
                self.index += 1
            elif char == '\\t':
                # 对制表符进行处理
                text_to_display = self.textEdit.toPlainText() + '\t'
            else:
                # 普通字符
                text_to_display = self.textEdit.toPlainText() + char

            # 添加光标（移除啦，加了总是有神奇bug）
            #text_to_display += '|' if self.cursorVisible else ''
            self.textEdit.setPlainText(text_to_display)
            self.index += 1
            self.textEdit.ensureCursorVisible()  # 始终滚动到底部
        else:
            self.timer.stop()
            #self.cursorTimer.stop()  # 停止光标闪烁


    def onScrollBarValueChanged(self, value):
        scroll_bar = self.textEdit.verticalScrollBar()
        self.userIsScrolling = value < scroll_bar.maximum()

def main():
    app = QApplication(sys.argv)
    filepaths = ['18503 copy.json']  # 替换为您的文件路径
    ex = TypewriterEffectApp(filepaths)
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
