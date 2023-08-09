import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog, QLineEdit, QCheckBox, QVBoxLayout 
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,600)
        self.setWindowTitle("Cadastro App")
        self.cadast = QPushButton("Cadastrar",self)
        self.cadast.setGeometry(200,490,400,100)
        self.cadast.clicked.connect(self.initSW)


    def initSW(self):
        self.second_window = SecondWindow()
        self.second_window.show()


class SecondWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("INFO")
        

    

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()