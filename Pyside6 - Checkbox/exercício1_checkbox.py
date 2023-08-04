import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QCheckBox, QVBoxLayout, QWidget
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Check Box")
        self.lbl = QLabel("Clique e aceite")
        self.ck = QCheckBox("Aceito")
        self.lbl2 = QLabel()


        layout = QVBoxLayout()
        layout.addWidget(self.lbl)
        layout.addWidget(self.ck)
        layout.addWidget(self.lbl2)


        container = QWidget()
        container.setLayout(layout)


        self.setCentralWidget(container)
        self.ck.stateChanged.connect(self.state)


    def state(self,s):


        if s == 2:
            self.lbl2.setText("Não aceito.")


        else:
            self.lbl2.setText("")
            

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
        
        