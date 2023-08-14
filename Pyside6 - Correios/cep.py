import brazilcep
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLineEdit, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle('Busca - CEP')


        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)


        self.lay = QVBoxLayout()
        self.central_widget.setLayout(self.lay)


        self.lbl_name = QLabel()
        self.lay.addWidget(self.lbl_name)


        self.input_name = QLineEdit()
        self.lay.addWidget(self.input_name)


        