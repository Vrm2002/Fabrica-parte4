from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Exercício 4 - Metros para Centrímetros")
        self.setGeometry(1000,750,1000,750)

        self.lbl = QLabel("Metros: ",self)
        font = self.lbl.font()
        font.setPointSize(25)
        self.lbl.setFont(font)
        self.lbl.setGeometry(100,100,155,40)

        self.input = QLineEdit(self)
        self.input.setGeometry(290,100,100,40)

        self.button = QPushButton("Converter",self)
        self.button.setGeometry(650,100,150,77)
        self.button.clicked.connect(self.convert)

        self.resultlbl = QLabel(self)
        self.resultlbl.setGeometry(650,190,155,40)

    def convert(self):
        

        try:

            num = float(self.input.text())
            result = num*100
            self.resultlbl.setText(f"Valor em centímetros: {result}")
        
        except ValueError:

            self.resultlbl.setText("Digite somente números.")


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()