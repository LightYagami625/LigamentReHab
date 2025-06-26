from PyQt5 import QtWidgets, QtCore
import sys

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Exercise Timer")
        self.setGeometry(100, 100, 300, 200)

        self.layout = QtWidgets.QVBoxLayout()

        self.label_seconds = QtWidgets.QLabel("Seconds: 0")
        self.layout.addWidget(self.label_seconds)

        self.label_message = QtWidgets.QLabel("Message: Ready")
        self.layout.addWidget(self.label_message)

        self.start_button = QtWidgets.QPushButton("Start")
        self.start_button.clicked.connect(self.start_timer)
        self.layout.addWidget(self.start_button)

        self.setLayout(self.layout)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.seconds = 0

    def start_timer(self):
        self.seconds = 0
        self.label_message.setText("Message: Timer Started")
        self.timer.start(1000)  # Update every second

    def update_timer(self):
        self.seconds += 1
        self.label_seconds.setText(f"Seconds: {self.seconds}")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())