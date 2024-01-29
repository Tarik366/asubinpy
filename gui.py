from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QWidget,QPushButton,QFrame,QMessageBox,QToolBar,QStatusBar
from PyQt6.QtCore import Qt,QSize,QCoreApplication
from PyQt6.QtGui import QIcon, QPixmap
import style_creator

class myWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Âsub-ı py")

        # Window sizing
        self.setMinimumSize(1000, 600)

        # Adding some css
        style_creator.create_css()
        with open("style/style-default.css","r") as file:
            self.setStyleSheet(file.read())
        try:
            with open("style/style.css","r") as file:
                self.setStyleSheet(file.read())
        except:
            pass

        self.setStatusBar(QStatusBar(self))

        menu_bar = self.menuBar()
        menu_bar.setStyleSheet("")

        file_menu = menu_bar.addMenu(f'&File')
        edit_menu = menu_bar.addMenu(f'&Edit')
        help_menu = menu_bar.addMenu(f'&Help')

    def onMyToolBarButtonClick(self, s):
        print("click", s)

from threading import Thread
import sys

app = QApplication(sys.argv)
window = myWin()
window.show()
sys.exit(app.exec())
