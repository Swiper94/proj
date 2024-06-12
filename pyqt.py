from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(0,0,1080,720)
    win.setWindowTitle("PyQt5")

    win.show()
    sys.exit(app.exec_())

window()