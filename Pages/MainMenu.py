from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from Pages.TablePageReaders import TablePageReaders
from Pages.TablePageBooks import TablePageBook
from PageTools import PageTools

class MainMenu(PageTools):
    def __init__(self):
        super().__init__()
        self.initThisWindow()
        self.initUI()

    def initUI(self):
        mainLayout = self.initMainLayout()
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        central_widget.setLayout(mainLayout)

    def initThisWindow(self):
        self.setWindowTitle("PyQtLibrary")
        self.setFixedSize(800, 600)

    def initButtonBar(self):
        buttonBar = QVBoxLayout()
        buttonBar.addWidget(
            self.mainMenuButton('Readers', lambda: self.pageView(TablePageReaders()))
        )
        buttonBar.addWidget(
            self.mainMenuButton('Books', lambda: self.pageView(TablePageBook()))
        )
        buttonBar.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return buttonBar

    def initLabel(self):
        label = QLabel()
        label.setText('PyQtLibrary')
        label.setFixedWidth(800)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        return label

    def initMainLayout(self):
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.initLabel())
        mainLayout.addLayout(self.initButtonBar())
        return mainLayout