import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("divisão de Números") #Titulo da tela.
        self.setGeometry(150, 150, 400, 230) #Tamanho da tela.

        self.label1 = QLabel("Número 1:", self)
        self.label1.setGeometry(10, 10, 80, 30) #Labels dizendo os números e suas dimensões 

        self.input1 = QLineEdit(self) #Caixa de input.
        self.input1.setGeometry(100, 10, 80, 30) #Tamanho da caixa de input.

        self.label2 = QLabel("Número 2:", self)
        self.label2.setGeometry(10, 50, 80, 30)

        self.input2 = QLineEdit(self)
        self.input2.setGeometry(100, 50, 80, 30)

        self.label3 = QLabel("Número 3:", self)
        self.label3.setGeometry(10, 90, 80, 30)

        self.input3 = QLineEdit(self)
        self.input3.setGeometry(100, 90, 80, 30)

        self.label4 = QLabel("Número 4:", self)
        self.label4.setGeometry(10, 130, 80, 30) 

        self.input4 = QLineEdit(self)
        self.input4.setGeometry(100, 130, 80, 30)


        self.result_label = QLabel(self) #Lbl de resultados
        self.result_label.setGeometry(100, 170, 280, 30) #dimensões.

        self.button = QPushButton("Calcular", self) #Botão de calcular.
        self.button.setGeometry(190, 10, 100, 70) #Dimensionamento do botão.
        self.button.clicked.connect(self.calcular_div) #Ao clicar no botão chama a função calcular_div


    def calcular_div(self): #Realiza a divisão


        num1 = float(self.input1.text()) #.text puxa o texto digitado.
        num2 = float(self.input2.text())
        num3 = float(self.input3.text())
        num4 = float(self.input4.text())
        div = (num1 + num2 + num3 + num4)/4
        self.result_label.setText(f"A soma é: {div}") #Informa o texto na tela ao clicar no botão.


if __name__ == "__main__": #Caso o nome da tela seja Main, executará primeiro.


    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())