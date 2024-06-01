from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt
from clsReader import Reader
from PageTools import PageTools
from library import library

class AddReaderPage(PageTools):
    def __init__(self):
        super().__init__()
        self.name = 'Name'
        self.surname = 'Surname'
        self.libraryCardNumber = 'Card number'
        self._initUI()

    def _initUI(self):
        mainLayout = self._initMainLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        mainLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        central_widget.setLayout(mainLayout)

    def _initMainLayout(self):
        mainLayout = QVBoxLayout()
        for var in [self.name, self.surname, self.libraryCardNumber]:
            mainLayout.addWidget(self._entering(var, var))
        mainLayout.addWidget(self.defaultButton(
            'Add Reader', 
            lambda: library.appendReader(Reader(
                self.name,
                self.surname,
                self.libraryCardNumber,
                []
            ))
        ))
        mainLayout.addWidget( self.defaultButton('Back', lambda: self.openReadersTable()))
        return mainLayout

    def _updateVariable(self, text, var):
        match var:
            case 'Name':
                self.name = text
            case 'Surname':
                self.surname = text
            case 'Card number':
                self.libraryCardNumber