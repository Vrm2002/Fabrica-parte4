from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QLineEdit
import sys

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Exercício 3 - Soma")
        self.setGeometry(1000,750,1000,750)

        self.label1 = QLabel("Nota 1:",self)
        font1 = self.label1.font()
        font1.setPointSize(25)
        self.label1.setFont(font1)
        self.label1.setGeometry(100,100,155,40)

        self.input1 = QLineEdit(self)
        self.input1.setGeometry(290,100,100,40)

        self.label2 = QLabel("Nota 2:",self)
        font2 = self.label2.font()
        font2.setPointSize(25)
        self.label2.setFont(font2)
        self.label2.setGeometry(100,250,155,40)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(290,250,100,40)

        self.label3 = QLabel("Nota 3:",self)
        font3 = self.label3.font()
        font3.setPointSize(25)
        self.label3.setFont(font3)
        self.label3.setGeometry(100,400,155,40)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(290,400,100,40)

        self.label4 = QLabel("Nota 4:",self)
        font4 = self.label4.font()
        font4.setPointSize(25)
        self.label4.setFont(font4)
        self.label4.setGeometry(100,550,155,40)

        self.input4 = QLineEdit(self)
        self.input4.setGeometry(290,550,100,40)

        self.button = QPushButton("Calcular",self)
        self.button.setGeometry(650,150,150,77)
        self.button.clicked.connect(self.calc)

        self.resultlabel = QLabel(self)
        self.resultlabel.setGeometry(650,250,155,40)


    def calc(self):


        try:
            num1 = float(self.input1.text())
            num2 = float(self.input2.text())
            num3 = float(self.input3.text())
            num4 = float(self.input4.text())
            result = (num1 + num2 + num3 + num4)/4
            self.resultlabel.setText(f"Resultado: {result}")
        
        except ValueError:
            self.resultlabel.setText("Digite somente números.")
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()