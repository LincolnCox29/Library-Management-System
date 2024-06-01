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

class AddBookPage(PageTools):
    def __init__(self):
        super().__init__()
        self.title = 'Title'
        self.author = 'Author'
        self.year = 'Year'
        self.pageCount = 'Number of pages'
        self.isbn = 'ISBN'
        self.copies = 'Copies'
        self._initUI()

    def _initUI(self):
        mainLayout = self._initMainLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        central_widget.setLayout(mainLayout)

    def _initMainLayout(self):
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self._choosingGenre())
        for var in [self.title, self.author, self.year, self.pageCount, self.isbn, self.copies]:
            mainLayout.addWidget(self._entering(var, var))
        mainLayout.addWidget(self.defaultButton(
            'Add Book', 
            lambda: library.appendBook(Book(
                self.title,
                self.author,
                self.year,
                self.textVarGenre.text(),
                self.pageCount,
                self.isbn,
                self.copies
            ))
        ))
        mainLayout.addWidget( self.defaultButton('Back', lambda: self.openBooksTable()))
        return mainLayout
    
    # region Genre
    def _choosingGenre(self):
        widget = QWidget()
        widget.setFixedWidth(270)
        field = QHBoxLayout()
        self.textVarGenre = QLabel()
        self.textVarGenre.setText('')
        field.addWidget(QLabel('Genre:'))
        field.addWidget(self.textVarGenre)
        field.addWidget(self._genreDropDownList())
        widget.setLayout(field)
        return widget
    
    def _genreDropDownList(self):
        combobox = QComboBox()
        combobox.addItems(genres)
        combobox.currentTextChanged.connect(self._updateGenreVariable)
        return combobox
    
    def _updateGenreVariable(self, value):
        self.textVarGenre.setText(value)
    # endregion

    # region Entering
    def _updateVariable(self, text, var):
        match var:
            case 'Title':
                self.title = text
            case 'Author':
                self.author = text
            case 'Year':
                self.year = text
            case 'Number of pages':
                self.pageCount = text
            case 'ISBN':
                self.isbn = text
            case 'Copies':
                self.copies = text
    # endregion