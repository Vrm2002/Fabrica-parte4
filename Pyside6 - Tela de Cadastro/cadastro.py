import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QFrame, QLineEdit, QCheckBox
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.cadastUI()
        self.conf(self)
        self.conf2(self)

    
    def cadastUI(self):


        self.setWindowTitle("Cadastro App")


        self.lbl = QLabel("Nome:",self)
        font = self.lbl.font()
        font.setPointSize(11)
        self.lbl.setFont(font)
        self.lbl.setGeometry(50,25,100,40)


        self.input = QLineEdit(self)
        self.input.setGeometry(99,35,670,20)


        self.lbl2 = QLabel("Telefone:",self)
        font2 = self.lbl2.font()
        font2.setPointSize(11)
        self.lbl2.setFont(font2)
        self.lbl2.setGeometry(34,50,100,40)

        
        self.input2 = QLineEdit(self)
        self.input2.setGeometry(99,60,670,20)


        self.lbl3 = QLabel("Endereço:",self)
        font3 = self.lbl3.font()
        font3.setPointSize(11)
        self.lbl3.setFont(font3)
        self.lbl3.setGeometry(30,75,100,40)


        self.input3 = QLineEdit(self)
        self.input3.setGeometry(99,85,670,20)


        self.lbl4 = QLabel("Masculino",self)
        font4 = self.lbl4.font()
        font4.setPointSize(11)
        self.lbl4.setFont(font4)
        self.lbl4.setGeometry(30,120,100,40)
        self.ck = QCheckBox(self)
        self.ck.setGeometry(100,93,100,100)
        self.ck.stateChanged.connect(self.conf)
    

        self.lbl5 = QLabel("Feminino",self)
        font5 = self.lbl5.font()
        font5.setPointSize(11)
        self.lbl5.setFont(font5)
        self.lbl5.setGeometry(130,120,100,40)
        self.ck2 = QCheckBox(self)
        self.ck2.setGeometry(195,93,100,100)
        self.ck2.stateChanged.connect(self.conf2)


        self.cadast = QPushButton("Cadastrar",self)
        self.cadast.setGeometry(200,490,400,100)
        self.cadast.clicked.connect(self.initSW)


    def initSW(self):


        window2 = SecondWindow()
        window2.addDockWidget()
        window2.show()




    def conf(self,x):


        if x == 2:
            self.ck.setChecked(True)
            self.ck2.setChecked(False)

        
        else:
            self.ck.setChecked(False)


    def conf2(self,y):


        if y == 2:
            self.ck2.setChecked(True)
            self.ck.setChecked(False)


        else:
            self.ck2.setChecked(False)


class SecondWindow(MainWindow):


    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.setWindowTitle("INFO.")



        self.lbl6 = QLabel(f"Nome: {self.input.text()}")
        font6 = self.lbl6.font()
        font6.setPointSize(11)
        self.lbl6.setFont(font6)
        self.lbl6.setGeometry(100,200,100,100)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()