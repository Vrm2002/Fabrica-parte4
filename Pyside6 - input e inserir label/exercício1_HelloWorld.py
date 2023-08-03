from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QLabel #Importa telas, funcionamento da aplicação, e o label que serve para ser o que está escrito na tela

from PySide6.QtCore import QSize, Qt

import sys

class MainWindow(QMainWindow):


    def __init__(self):


        super().__init__()
        self.setWindowTitle("exercicio 1") #Nome da tela.
        self.setFixedSize(600,400) #Tamanho fixo da tela.
        self.lbl = QLabel("Hello World!") #O que ta escrito na tela.
        font = self.lbl.font()
        font.setPointSize(35) #Seta o tamanho da fonte
        self.lbl.setFont(font) #Coloca a fonte na label
        self.lbl.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) #Alinha a fonte
        self.setCentralWidget(self.lbl) #Centraliza o todo, para aparecer na tela.

app = QApplication(sys.argv) #Atribui a classe QApplication com os argumntos sys.argv para a var app
janela = MainWindow() #Atribui a classe MainWindow para a variável janela.
janela.show() #Executa a classe MainWindow
app.exec() #Faz a aplicação rodar.
