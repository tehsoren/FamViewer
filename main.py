import sys
from PyQt5.QtWidgets import QApplication

import MainWindow

def StartMainWindow():
    app = QApplication([])
    mainWindow = MainWindow.MainWindow()

    app.exec_()

if __name__ == "__main__":
    StartMainWindow()
