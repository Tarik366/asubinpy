from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QDesktopWidget, QWidget,QPushButton,QFrame,QMessageBox
from PyQt5.QtCore import Qt,QSize,QCoreApplication
from PyQt5.QtGui import QIcon, QPixmap

class myWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Âsub-ı py")

        # Window sizing
        screen = QDesktopWidget().screenGeometry()
        self.setMinimumSize(1000, 600)
        x = (screen.width() - self.width()) // 2
        y = screen.height() - self.height() // 2
        self.move(x, y)

        

from threading import Thread
import sys

app = QApplication(sys.argv)
window = myWin()
window.show()
sys.exit(app.exec())
