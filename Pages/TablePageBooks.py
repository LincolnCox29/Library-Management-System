from PyQt6.QtWidgets import QWidget, QTableWidgetItem, QHBoxLayout, QMenu, QTableWidget, QAbstractItemView
from library import library
from AbstractTablePage import AbstractTablePage
from Pages.AddBookPage import AddBookPage
from Pages.BookInfoPage import BookInfoPage
from clsBook import Book
from PyQt6.QtCore import Qt, QPoint

class TablePageBook(AbstractTablePage):
    def __init__(self):
        self.columnCount = 7
        self.tabularArray = library.booksList
        self.infoPageType = BookInfoPage
        super().__init__()

    def tableFilling(self, table):
        for row in range(len(library.booksList)):
            for col in range(7):
                match col:
                    case 0:
                        item = QTableWidgetItem(library.booksList[row].name)
                    case 1:
                        item = QTableWidgetItem(library.booksList[row].author)
                    case 2:
                        item = QTableWidgetItem(str(library.booksList[row].year))
                    case 3:
                        item = QTableWidgetItem(library.booksList[row].genre)
                    case 4:
                        item = QTableWidgetItem(str(library.booksList[row].pageCount))
                    case 5:
                        item = QTableWidgetItem(str(library.booksList[row].isbn))
                    case 6:
                        item = QTableWidgetItem(str(library.booksList[row].copies))
                item.setFlags(item.flags() ^ Qt.ItemFlag.ItemIsEditable)
                table.setItem(row, col, item)
        new_headers = ['Title', 'Author', 'Year', 'Genre', 'Number of pages', 'ISBN', 'Copies']
        table.setHorizontalHeaderLabels(new_headers)
        self.table : QTableWidget = table
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.showContextMenu)
        table.clicked.connect(self._itemClicked)
        return table
    
    def buttonBur(self):
        buttonBarLayout = QHBoxLayout()
        buttonBar = QWidget()
        buttonBarLayout.addWidget(self.defaultButton('Back', lambda: self.openMainMenu()))
        buttonBarLayout.addWidget(self.defaultButton('Add book', lambda: self.pageView(AddBookPage())))
        buttonBar.setLayout(buttonBarLayout)
        return buttonBar
    
    def showContextMenu(self, ClickPos: QPoint):
        contextMenu = QMenu(self)
        contextMenu.addAction('Del Copie').triggered.connect(lambda: self.delCopy(ClickPos))
        contextMenu.addAction('Add Copie').triggered.connect(lambda: self.addCopy(ClickPos))
        contextMenu.addAction('Del Book').triggered.connect(lambda: self.delBook(ClickPos))
        contextMenu.exec(self.table.mapToGlobal(ClickPos))

    def addCopy(self, ClickPos):
        if self.table.itemAt(ClickPos) != None:
            book = self.table.itemAt(ClickPos).row()
            library.booksList[book].appendCopy()
            self.table.setItem(book, 6, QTableWidgetItem(str(library.booksList[book].copies)))
        
    def delCopy(self, ClickPos):
        if self.table.itemAt(ClickPos) != None:
            book = self.table.itemAt(ClickPos).row()
            library.booksList[book].delCopy()
            if library.booksList[book].copies <= 0:
                library.delBook(library.booksList[book])
                self.table.removeRow(book)
            else:
                self.table.setItem(book, 6, QTableWidgetItem(str(library.booksList[book].copies)))

    def delBook(self, ClickPos):
        if self.table.itemAt(ClickPos) != None:
            book = self.table.itemAt(ClickPos).row()
            library.delBook(library.booksList[book])
            self.table.removeRow(book)