from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
from PySide6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Exercício 3 - Soma")
        self.setGeometry(1000,750,1000,750)

        self.label1 = QLabel("Número 1:",self)
        font1 = self.label1.font()
        font1.setPointSize(25)
        self.label1.setFont(font1)
        self.label1.setGeometry(100,100,155,40)
        self.label1.setScaledContents(True)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(290,100,100,40)

        self.label2 = QLabel("Número 2:",self)
        font2 = self.label2.font()
        font2.setPointSize(25)
        self.label2.setFont(font2)
        self.label2.setGeometry(100,250,155,40)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(290,250,100,40)

        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(650,150,150,77)
        self.button.clicked.connect(self.calc)


    def calc(self):
        





app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()