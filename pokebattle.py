from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtCore import  Qt
from PySide6.QtGui import QPixmap
import sys


class BattleWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Pokemon Battle Screen")
        self.lbl = QLabel()
        self.lbl.setPixmap(QPixmap("battleground.jpg"))
        self.lbl.setScaledContents(True)
        self.setCentralWidget(self.lbl)

app = QApplication(sys.argv)
battle_window = BattleWindow()
battle_window.show()
app.exec()
