import sys
from PyQt5.QtWidgets import QApplication

import MainWindow

def StartMainWindow(file_path):
    app = QApplication([])
    mainWindow = MainWindow.MainWindow(file_path)

    app.exec_()

if __name__ == "__main__":
    file_path= "E:\\fam\\18jun.ged"
    StartMainWindow(file_path)
