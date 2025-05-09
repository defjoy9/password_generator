import string
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QLineEdit
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password_Generator")
        self.setGeometry(700,300,500,500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Generate",self)
        self.uppercase = QCheckBox("Uppercase", self)
        self.lowercase = QCheckBox("Lowercase", self)
        self.numbers = QCheckBox("Numbers", self)
        self.symbols = QCheckBox("Symbols", self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(50,20,400,50)
        self.button.setGeometry(200,150,100,40)
        self.uppercase.setGeometry(60,50,500,100)
        self.lowercase.setGeometry(160,50,500,100)
        self.numbers.setGeometry(260,50,500,100)
        self.symbols.setGeometry(360,50,500,100)

        self.button.clicked.connect(self.generate_password)
        self.uppercase.stateChanged.connect(self.generate_password)
        self.lowercase.stateChanged.connect(self.generate_password)
        self.numbers.stateChanged.connect(self.generate_password)
        self.symbols.stateChanged.connect(self.generate_password)

    def generate_password(self):
        all_chars = ""
        length = 16

        if self.uppercase.isChecked():
            all_chars += string.ascii_uppercase
        if self.lowercase.isChecked():
            all_chars += string.ascii_lowercase
        if self.numbers.isChecked():
            all_chars += string.digits
        if self.symbols.isChecked():
            all_chars += string.punctuation

        if not all_chars:
            self.line_edit.setText("Select at least one option.")
            return

        password = ''.join(random.choice(all_chars) for _ in range(length))
        self.line_edit.setText(password)
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()