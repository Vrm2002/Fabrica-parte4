from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PySide6.QtCore import  Qt
import sys


class BattleWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setWindowTitle("Pokemon Battle Screen")
        self.setGeometry(1000,750,1000,750)

app = QApplication(sys.argv)
battle_window = BattleWindow()
battle_window.show()
app.exec()