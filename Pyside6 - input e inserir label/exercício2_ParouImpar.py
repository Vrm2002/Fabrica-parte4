from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel, QPushButton

from PySide6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):


    def __init__(self):


        super().__init__()
        self.setWindowTitle("exercicio 2")

        self.button = QPushButton('Button',self) #Cria o botão
        self.button.setGeometry(190,10,100,70) #Dimensões e posicionamento do botão.
        self.setFixedSize(600,400) #Tamanho fixo da tela.
        self.result_label = QLabel(self) #Lbl de resultados.
        self.result_label.setGeometry(10,90,280,30) #Dimensionamento e posicionamento da Lbl


        self.button.clicked.connect(self.imprimir)


    def imprimir(self): #Texto que aparece na lbl


        numero = 4
        if numero % 2 == 0:
            self.result_label.setText(f'Este numero e {numero} par')
        else:
            self.result_label.setText(f'Este numero e {numero} impar')


app = QApplication(sys.argv)
janela = MainWindow()
janela.show()
app.exec()