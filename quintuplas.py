from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog
from PySide6.QtGui import QPixmap
import sys 

class quintuplas_apicacao(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Quintuplas DEX')
        self.setFixedSize(800,600)

        self.button_ichika = QPushButton('Nakano Ichika',self)
        self.button_ichika.setGeometry(200,400,100,100)

        self.button_nino = QPushButton('Nakano Nino',self)
        self.button_nino.setGeometry(500,400,100,100)

        self.button_miku = QPushButton('Nakano Miku',self)
        self.button_miku.setGeometry(200,100,100,100)

        self.button_yotsuba = QPushButton('Nakano Yotsuba',self)
        self.button_yotsuba.setGeometry(350,250,100,100)

        self.button_itsuki = QPushButton('Nakano Itsuki',self)
        self.button_itsuki.setGeometry(500,100,100,100)


        self.button_ichika.clicked.connect(self.ichika_label)
        self.button_nino.clicked.connect(self.nino_label)
        self.button_miku.clicked.connect(self.miku_label)
        self.button_yotsuba.clicked.connect(self.yotsuba_label)
        self.button_itsuki.clicked.connect(self.itsuki_label)
        

    def ichika_label(self):
        pass 


    def nino_label(self):
        pass


    def miku_label(self):
        pass


    def yotsuba_label(self):
        pass

    
    def itsuki_label(self):
        pass







if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = quintuplas_apicacao()
    janela.show()
    app.exec()
