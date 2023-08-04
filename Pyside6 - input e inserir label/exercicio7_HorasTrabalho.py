from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Exercício 7 - Área do Quadrado.")
        self.setGeometry(1000,750,1000,750)

        self.lbl = QLabel("Salário por Hora:",self)
        font = self.lbl.font()
        font.setPointSize(25)
        self.lbl.setFont(font)
        self.lbl.setGeometry(100,100,270,40)

        self.input = QLineEdit(self)
        self.input.setGeometry(378,100,100,40)

        self.lbl2 = QLabel("Horas Trabalhadas:",self)
        font2 = self.lbl2.font()
        font2.setPointSize(25)
        self.lbl2.setFont(font2)
        self.lbl2.setGeometry(100,250,270,40)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(378,250,100,40)

        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(650,100,150,77)
        self.button.clicked.connect(self.calc)

        self.resultlbl = QLabel(self)
        self.resultlbl.setGeometry(650,190,170,40)

    
    def calc(self):


        try:


            sal = float(self.input.text())
            hor = float(self.input2.text())
            result = sal * hor
            self.resultlbl.setText(f"O seu salário total é {result}")


        except ValueError:


            self.resultlbl.setText("Digite somente números")

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()