from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, 
    QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QPushButton, QHBoxLayout, 
    QComboBox,QLineEdit, QSizePolicy, QScrollArea, QMenu
) 
from PyQt6.QtCore import Qt, QPoint
from genres import genres
from clsBook import Book
from clsReader import Reader
from PageTools import PageTools
from library import library

class ReaderInfoPage(PageTools):
    def __init__(self, reader : Reader):
        super().__init__()
        self._reader = reader
        self._initUI()

    def _initUI(self):
        scrollArea = QScrollArea(self)
        scrollArea.setWidgetResizable(True)
        self.mainLayout = self._initMainLayout()
        centralWidget = QWidget(self)
        scrollArea.setWidget(centralWidget)
        self.setCentralWidget(scrollArea)
        self.mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        centralWidget.setLayout(self.mainLayout)

    def _initMainLayout(self):
        self.mainLayout = QVBoxLayout()
        fields = [
            ['Name', self._reader.name],
            ['Surname', self._reader.surname],
            ['Library card number', self._reader.libraryCardNumber]
        ]
        for field in fields:
            self.mainLayout.addWidget(self._textField(str(field[0]), str(field[1])))
        self.mainLayout.addWidget(self._backButton())
        self.mainLayout.addWidget(self._delReaderButton())
        for book in self._reader.booksList:
            self.mainLayout.addWidget(self._bookLabel(book))
        return self.mainLayout

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

    def _bookLabel(self, book : Book):
        bookLabel = QLabel(str(book))
        bookLabel.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        bookLabel.customContextMenuRequested.connect(lambda pos: self._bookLabelContextMenu(book, bookLabel, pos))
        return bookLabel

    def _bookLabelContextMenu(self, book : Book, label : QLabel, pos : QPoint):
        contextMenu = QMenu(self)
        contextMenu.addAction('Del Book').triggered.connect(lambda: self.returnBook(book, label))
        contextMenu.exec(label.mapToGlobal(pos))

    def returnBook(self, book : Book, label : QLabel):
        self._reader.returnBook(library, book)
        self.mainLayout.removeWidget(label)
        label.deleteLater()