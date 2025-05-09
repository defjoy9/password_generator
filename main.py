import string
import random
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password_Generator")
        self.setGeometry(700,300,500,500)


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

# if __name__ == "__main__":
#     main()
