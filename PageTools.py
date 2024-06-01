from PyQt6.QtWidgets import QPushButton, QMainWindow, QHeaderView, QTableWidget, QWidget, QLineEdit, QLabel, QHBoxLayout, QMessageBox
from library import library, saveLibraryToJson
from PyQt6.QtCore import Qt

class PageTools(QMainWindow):

    def initThisWindow(self):
        self.setWindowTitle("PyQtLibrary")
        self.setGeometry(100, 100, 800, 600)

    def pageView(self, _newWindow : QMainWindow):
        x = self.x()
        y = self.y()
        self.close()
        self.window = _newWindow
        self.setWindowTitle("PyQtLibrary")
        self.window.setFixedSize(self.size())
        self.window.move(x, y)
        self.window.show()
    
    def mainMenuButton(self, text : str, onClick):
        button = QPushButton()
        button.setText(text)
        button.clicked.connect(onClick)
        button.setFixedWidth(600)
        button.setFixedHeight(100)
        return button
    
    def openMainMenu(self):
        from Pages.MainMenu import MainMenu
        self.pageView(MainMenu())

    def openBooksTable(self):
        from Pages.TablePageBooks import TablePageBook
        self.pageView(TablePageBook())

    def openReadersTable(self):
        from Pages.TablePageReaders import TablePageReaders
        self.pageView(TablePageReaders())

    def defaultButton(self, text, onClick):
        button = QPushButton()
        button.setText(text)
        button.clicked.connect(onClick)
        return button
    
    def _entering(self, label, var):
        widget = QWidget()
        widget.setFixedWidth(250)
        field = QHBoxLayout()
        textbox = QLineEdit()
        textbox.textChanged.connect( lambda: self._updateVariable(textbox.text(), var))
        field.addWidget(QLabel(f'{label}:'))
        field.addWidget(textbox)
        widget.setLayout(field)
        return widget
    
    def closeEvent(self, event):
        saveLibraryToJson()
