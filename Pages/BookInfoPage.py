from PyQt6.QtWidgets import (
    QMainWindow, QVBoxLayout, QWidget, 
    QLabel, QTableWidget, QTableWidgetItem, 
    QHeaderView, QPushButton, QHBoxLayout, 
    QComboBox,QLineEdit, QSizePolicy
) 
from PyQt6.QtCore import Qt
from genres import genres
from clsBook import Book
from PageTools import PageTools
from library import library

class BookInfoPage(PageTools):
    def __init__(self, book : Book):
        super().__init__()
        self._book = book
        self.readerMap = {}
        self._initUI()

    def _initUI(self):
        mainLayout = self._initMainLayout()
        central_widget = QWidget(self)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(mainLayout)

    def _initMainLayout(self):
        mainLayout = QVBoxLayout()
        self.bookText = QLabel(str(self._book))
        mainLayout.addWidget(self.bookText)
        mainLayout.addWidget(self.backButton())
        mainLayout.addWidget(self.delCopyButton())
        mainLayout.addWidget(self.addCopyButton())
        mainLayout.addWidget(self.giveBookWidget())
        return mainLayout
    
    def backButton(self):
        backButton = self.defaultButton('Back', self.openBooksTable)
        backButton.setFixedSize(100, 25)
        return backButton

    def giveBookWidget(self):
        self.readerComboBox = QComboBox()
        self.readerComboBox.setPlaceholderText('Give the book to the reader')
        self.readerComboBox.setFixedWidth(200)
        for index, reader in enumerate(library.readersList):
            if not reader.checkingBookForAvailability(self._book):
                self.readerComboBox.addItem(str(reader))
                self.readerMap[index] = reader
        self.readerComboBox.activated.connect(self.addReaderToGiveBookWidget)
        return self.readerComboBox
    
    def addReaderToGiveBookWidget(self, index):
        selectedReader = self.readerMap.get(index)
        if selectedReader:
            selectedReader.takeBook(library, self._book)
            self.openBooksTable()
    
    def addCopyButton(self):
        addCopyButton = self.defaultButton('Add Copy', self._addCopy)
        addCopyButton.setFixedSize(100, 25)
        return addCopyButton
    
    def delCopyButton(self):
        delCopyButton = self.defaultButton('Del Copy', self._delCopy)
        delCopyButton.setFixedSize(100, 25)
        return delCopyButton
    
    def _addCopy(self):
        self._book.appendCopy()
        self._updateBookText()
    
    def _delCopy(self):
        self._book.delCopy()
        self._updateBookText()
    
    def _updateBookText(self):
        if self._book.copies == 0:
            library.delBook(self._book)
            self.openBooksTable()
        self.bookText.setText(str(self._book))