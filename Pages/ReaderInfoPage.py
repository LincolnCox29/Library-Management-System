from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, 
    QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QPushButton, QHBoxLayout, 
    QComboBox,QLineEdit
) 
from PyQt6.QtCore import Qt
from genres import genres
from clsReader import Reader
from PageTools import PageTools
from library import library

class ReaderInfoPage(QMainWindow, PageTools):
    def __init__(self, reader : Reader):
        super().__init__()
        self._reader = reader