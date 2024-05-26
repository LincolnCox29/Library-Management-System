from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, 
    QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QPushButton, QHBoxLayout, 
    QComboBox,QLineEdit
) 
from PyQt6.QtCore import Qt
from genres import genres
from clsBook import Book
from PageTools import PageTools
from library import library

class BookInfoPage(QMainWindow, PageTools):
    def __init__(self, book : Book):
        super().__init__()
        self._book = book