import brazilcep
from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Busca - CEP')
        self.CepUi(self)

    
    def CepUi(self):


        
