from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QDialog
from PySide6.QtGui import QPixmap, Qt
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
        self.window_ichika = quintuplas_dialog('Nakano Ichika','Ichika.jpg')
        self.window_ichika.show()


    def nino_label(self):
        self.window_nino = quintuplas_dialog('Nakano Nino', 'Nino.jpg')
        self.window_nino.show()


    def miku_label(self):
        self.window_miku = quintuplas_dialog('Nakano Miku', 'Miku.png')
        self.window_miku.show()


    def yotsuba_label(self):
        self.window_yotsuba = quintuplas_dialog('Nakano Yotsuba', 'Yotsuba.jpg')
        self.window_yotsuba.show()

    
    def itsuki_label(self):
        self.window_itsuki = quintuplas_dialog('Nakano Itsuki', 'Itsuki.png')
        self.window_itsuki.show()


class quintuplas_dialog(QDialog):
    def __init__(self, ui_name, image_url):
        super().__init__()

        self.setWindowTitle(ui_name)
        self.setFixedSize(800,600)

        self.img_label = QLabel(self)
        self.img_label.setFixedSize(800,600)
        pixmap = QPixmap(image_url)
        self.img_label.setPixmap(pixmap)
        self.img_label.setScaledContents(True)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    janela = quintuplas_apicacao()
    janela.show()
    app.exec()
