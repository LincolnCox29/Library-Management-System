from clsBook import Book
from clsLibrary import Library
from clsReader import Reader
from sys import argv
from Pages.MainMenu import MainMenu
from PyQt6.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(argv)
    window = MainMenu()
    window.show()
    app.exec()