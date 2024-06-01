from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout
from PyQt6.QtCore import Qt, QModelIndex
from PageTools import PageTools
from library import library

class AbstractTablePage(PageTools):
    def __init__(self):
        super().__init__()
        self.initThisWindow()
        self._initUI()

    def _initUI(self):
        mainLayout = self._initMainLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(mainLayout)

    def _initMainLayout(self):
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.initTable(self.columnCount, self.tabularArray))
        mainLayout.addWidget(self.buttonBur())
        mainLayout.addLayout(QVBoxLayout())
        return mainLayout

    def tableFilling(self, table):
        pass ## OVERRIDE ##

    def buttonBur(self):
        pass ## OVERRIDE ##
    
    def initTable(self, numberOfColumns : int, tabularArray : list):
        table = QTableWidget(self)
        table.setGeometry(50, 50, 500, 300)
        table.setRowCount(len(tabularArray))
        table.setColumnCount(numberOfColumns)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        table.setSelectionBehavior(QTableWidget.SelectionBehavior.SelectRows)
        table = self.tableFilling(table)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        return table
    
    def _itemClicked(self, item : QModelIndex):
        if item.row() != None and Qt.MouseButton.LeftButton:
            self.pageView(self.infoPageType(self.tabularArray[item.row()]))