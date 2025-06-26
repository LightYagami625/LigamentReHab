from PyQt5 import QtWidgets, QtCore
import sys
from ui import MainWindow

class App(QtWidgets.QApplication):
    def __init__(self, argv):
        super().__init__(argv)
        self.window = MainWindow()
        self.window.show()

if __name__ == "__main__":
    app = App(sys.argv)
    sys.exit(app.exec_())