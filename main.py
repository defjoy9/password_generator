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
        self.button = QPushButton("Copy Password",self)
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

        self.uppercase.stateChanged.connect(self.checkbox_changed)
        self.lowercase.stateChanged.connect(self.checkbox_changed)
        self.numbers.stateChanged.connect(self.checkbox_changed)
        self.symbols.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self, state):
        sender = self.sender()  # Gets the checkbox that sent the signal
        all_chars = ""
        if sender == self.uppercase:
            if state == Qt.Checked:
                all_chars += string.ascii_uppercase 
        elif sender == self.lowercase:
            if state == Qt.Checked:
                all_chars += string.ascii_lowercase 
        elif sender == self.numbers:
            if state == Qt.Checked:
                all_chars += string.digits 
        elif sender == self.symbols:
            if state == Qt.Checked:
                all_chars += string.punctuation 

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()


# class Password_Generator:
#     def __init__(self, length=12, uppercase=True, lowercase=True, number=True, symbols=True):
#         self.length = length
#         self.uppercase = uppercase
#         self.lowercase = lowercase
#         self.number = number
#         self.symbols = symbols

#     def generate(self):
#         all_chars = ""

#         if self.uppercase:
#             all_chars += string.ascii_uppercase
#         if self.lowercase:
#             all_chars += string.ascii_lowercase
#         if self.number:
#             all_chars += string.digits
#         if self.symbols:
#             all_chars += string.punctuation

#         password = ''.join(random.choice(all_chars) for _ in range(self.length))
#         return password

# def main():
#     password_gen = Password_Generator(length=16, uppercase=True, lowercase=True, number=True, symbols=True)
#     new_password = password_gen.generate()

#     print(new_password)
