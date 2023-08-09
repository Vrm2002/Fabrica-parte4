import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout
from PySide6.QtGui import QPixmap
from rectanglewindow import RectWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.ui()

    
    def ui(self):
        self.setWindowTitle("App - Calculo de Área")


        layout = QVBoxLayout()


        self.lbl = QLabel("Escolha a forma!",self)
        font = self.lbl.font()
        font.setPointSize(11)
        self.lbl.setFont(font)
        self.lbl.setGeometry(330,120,250,40)
        layout.addWidget(self.lbl)


        self.button = QPushButton("Retângulo",self)
        self.button.setGeometry(150,200,150,40)
        self.button.clicked.connect(self.rectan_window_connect)
        layout.addWidget(self.button)

        
        self.button2 = QPushButton("Círculo",self)
        self.button2.setGeometry(480,200,150,40)
        self.button2.clicked.connect(self.circle_window_connect)
        layout.addWidget(self.button2)


        image_lbl = QLabel(self)
        pixmap = QPixmap("circulo.png")
        image_lbl.setPixmap(pixmap)
        image_lbl.setGeometry(480,250,150,150)
        image_lbl.setScaledContents(True)
        layout.addWidget(image_lbl)


        image_lbl2 = QLabel(self)
        pixmap2 = QPixmap("retangulo.png")
        image_lbl2.setPixmap(pixmap2)
        image_lbl2.setGeometry(150,250,150,150)
        image_lbl2.setScaledContents(True)
        layout.addWidget(image_lbl2)


        self.setLayout = layout


    def circle_window_connect(self):
        pass


    def rectan_window_connect(self):
        self.rect_window = RectWindow()
        self.rect_window.show


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()