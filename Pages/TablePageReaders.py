from PyQt6.QtWidgets import( 
    QMainWindow, QVBoxLayout,
    QWidget, QLabel, QTableWidget, 
    QTableWidgetItem, QHeaderView, QPushButton,
      QHBoxLayout, QMenu, QApplication, QAbstractItemView
)
from Pages.ReaderInfoPage import ReaderInfoPage
from PyQt6.QtCore import Qt, QPoint, QModelIndex
from Pages.AddReaderPage import AddReaderPage
from AbstractTablePage import AbstractTablePage
from library import library

class TablePageReaders(AbstractTablePage):
    def __init__(self):
        self.columnCount = 3
        self.tabularArray = library.readersList
        self.infoPageType = ReaderInfoPage
        super().__init__()

    def tableFilling(self, table):
        for row in range(len(library.readersList)):
            for col in range(3):
                match col:
                    case 0:
                        item = QTableWidgetItem(library.readersList[row].name)
                    case 1:
                        item = QTableWidgetItem(library.readersList[row].surname)
                    case 2:
                        item = QTableWidgetItem(str(library.readersList[row].libraryCardNumber))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
        new_headers = ['Name', 'SurName', 'Card number']
        table.setHorizontalHeaderLabels(new_headers)
        self.table : QTableWidget = table
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.customContextMenuRequested.connect(self.showContextMenu)
        table.clicked.connect(self._itemClicked)
        return table
    
    def buttonBur(self):
        buttonBarLayout = QHBoxLayout()
        buttonBar = QWidget()
        buttonBarLayout.addWidget(self.defaultButton('Back', lambda: self.openMainMenu()))
        buttonBarLayout.addWidget(self.defaultButton('Add reader', lambda: self.pageView(AddReaderPage())))
        buttonBar.setLayout(buttonBarLayout)
        return buttonBar
    
    def showContextMenu(self, ClickPos: QPoint):
        contextMenu = QMenu(self)
        delReader = contextMenu.addAction('Del Reader')
        delReader.triggered.connect(lambda: self.delReader(ClickPos))
        contextMenu.exec(self.table.mapToGlobal(ClickPos))

    def delReader(self, ClickPos : QPoint):
        if self.table.itemAt(ClickPos) is not None:
            reader = self.table.itemAt(ClickPos).row()
            library.delReader(library.readersList[reader])
            self.table.removeRow(reader)