from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Exercício 7 - Área do Quadrado.")
        self.setGeometry(1000,750,1000,750)

        self.lbl = QLabel("Lado:",self)
        font = self.lbl.font()
        font.setPointSize(25)
        self.lbl.setFont(font)
        self.lbl.setGeometry(100,100,230,40)

        self.input = QLineEdit(self)
        self.input.setGeometry(250,100,100,40)

        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(650,100,150,77)
        self.button.clicked.connect(self.calc)

        self.resultlbl = QLabel(self)
        self.resultlbl.setGeometry(650,190,170,40)

    
    def calc(self):
        
        try:

            num = float(self.input.text())
            result = num**2
            self.resultlbl.setText(f"A área do quadrado é {result}")

        except ValueError:
            
            self.resultlbl.setText("Digite somente números.")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()