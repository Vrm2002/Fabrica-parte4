from rectangle import *
from PySide6.QtWidgets import QDialog

class RectWindow(QDialog):
    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.rect_ui()

    
    def rect_ui(self):


        self.setWindowTitle("App - Cálculo Área do Retângulo")