import sys
from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.UI()

    
    def UI(self):


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
        layout.addWidget(self.button)

        
        self.button2 = QPushButton("Círculo",self)
        self.button2.setGeometry(480,200,150,40)
        layout.addWidget(self.button2)


        self.setLayout = layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()