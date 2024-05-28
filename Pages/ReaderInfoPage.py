from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, 
    QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QPushButton, QHBoxLayout, 
    QComboBox,QLineEdit, QSizePolicy, QScrollArea
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
        self._initUI()

    def _initUI(self):
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        mainLayout = self._initMainLayout()
        central_widget = QWidget(self)
        scrollArea.setWidget(central_widget)
        self.setCentralWidget(scrollArea)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        central_widget.setLayout(mainLayout)

    def _initMainLayout(self):
        mainLayout = QVBoxLayout()
        fields = [
            ['Name', self._reader.name],
            ['Surname', self._reader.surname],
            ['Library card number', self._reader.libraryCardNumber]
        ]
        for field in fields:
            mainLayout.addWidget(self._textField(str(field[0]), str(field[1])))
        mainLayout.addWidget(self._backButton())
        mainLayout.addWidget(self._delReaderButton())
        for book in self._reader.booksList:
            mainLayout.addWidget(QLabel(str(book)))
        return mainLayout

    def _textField(self, label : str, value : str):
        widget = QWidget()
        field = QHBoxLayout()
        field.setAlignment(Qt.AlignmentFlag.AlignLeft)
        field.addWidget(QLabel(f'{label}:'))
        field.addWidget(QLabel(value))
        widget.setLayout(field)
        return widget

    def _backButton(self):
        backButton = self.defaultButton('Back', self.openReadersTable)
        backButton.setFixedSize(100, 25)
        return backButton
    
    def _delReaderButton(self):
        delReaderButton = self.defaultButton('Del Reader', self._delReader)
        delReaderButton.setFixedSize(100, 25)
        return delReaderButton

    def _delReader(self):
        library.delReader(self._reader)
        self.openReadersTable()


