import sys
from PyQt5.QtWidgets import QApplication

import MainWindow

def StartMainWindow(file_path =None):
    app = QApplication([])
    mainWindow = MainWindow.MainWindow(file_path)
    
    app.exec_()

if __name__ == "__main__":
    print(sys.argv)
    if(len(sys.argv)>1):
        StartMainWindow(sys.argv[1])
    else:
        StartMainWindow()
