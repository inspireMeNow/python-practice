import sys
from PyQt6.QtWidgets import QMessageBox,QApplication,QWidget,QToolTip,QPushButton
from PyQt6.QtGui import QFont

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        QToolTip.setFont(QFont('JetBrains Miono',12))
        self.setToolTip('this is a <b>QWidget</b> widget')
        btn = QPushButton('Button',self)
        btn.setToolTip('this is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50,50)
        qbtn = QPushButton('Quit',self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150,50)
        # self.statusBar
        self.setGeometry(300,300,300,200)
        self.setWindowTitle('Tooltips')
        self.show()
    
    def closeEvent(self,event):
        reply = QMessageBox.question(self,'Message',"Are you sure to qiut?",QMessageBox.StandardButton.Yes|QMessageBox.StandardButton.No)
        if reply == QMessageBox.StandardButton.Yes:
            event.accept()
        else:
            event.ignore()
    
    def center(self):
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
def main():
    app = QApplication(sys.argv)
    # w = QWidget()
    # w.resize(250,200)
    # w.move(300,300)
    # w.setWindowTitle('hello')
    # w.show()
    ex = Example()
    sys.exit(app.exec())
if __name__ == '__main__':
    main()