import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QDialog, QLineEdit, QCheckBox, QVBoxLayout 
from PySide6.QtGui import QPixmap


class MainWindow(QMainWindow):


    def __init__(self):
        super().__init__()


        self.setFixedSize(800,600)
        self.cadastUI()

    
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
        self.second_window = SecondWindow()


        name = self.input.text()
        phone = self.input2.text()
        adress = self.input3.text()


        if self.ck.isChecked() and not self.ck2.isChecked():
            sex = "Másculino"
            self.second_window.UiInfo(name,phone,adress,sex)
            self.second_window.show()


        elif self.ck2.isChecked() and not self.ck.isChecked():
            sex = "Feminino"
            self.second_window.UiInfo(name,phone,adress,sex)
            self.second_window.show()
        

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


class SecondWindow(QDialog):


    def __init__(self):
        super().__init__()
        self.setWindowTitle("INFO")
        self.setFixedSize(800,600)

    
    def UiInfo(self,name,phone,adress,sex):


        layout = QVBoxLayout()


        self.lbl6 = QLabel(f"Nome: {name}",self)
        font6 = self.lbl6.font()
        font6.setPointSize(11)
        self.lbl6.setFont(font6)
        self.lbl6.setGeometry(90,100,250,40)
        layout.addWidget(self.lbl6)


        self.lbl7 = QLabel(f"Telefone: {phone}",self)
        font7 = self.lbl7.font()
        font7.setPointSize(11)
        self.lbl7.setFont(font7)
        self.lbl7.setGeometry(90,200,250,40)
        layout.addWidget(self.lbl7)


        self.lbl8 = QLabel(f"Endereço: {adress}",self)
        font8 = self.lbl8.font()
        font8.setPointSize(11)
        self.lbl8.setFont(font8)
        self.lbl8.setGeometry(90,300,250,40)
        layout.addWidget(self.lbl8)


        self.lbl9 = QLabel(f"Sexo: {sex}",self)
        font9 = self.lbl9.font()
        font9.setPointSize(11)
        self.lbl9.setFont(font9)
        self.lbl9.setGeometry(90,400,250,40)
        layout.addWidget(self.lbl9)


        image_label = QLabel(self)
        pixmap = QPixmap("picachu.png")
        image_label.setPixmap(pixmap)
        image_label.setGeometry(400,90,300,400)
        image_label.setScaledContents(True)
        layout.addWidget(image_label)


        self.setLayout = layout


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()