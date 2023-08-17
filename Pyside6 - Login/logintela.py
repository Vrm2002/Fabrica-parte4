# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logintela.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QSizePolicy, QVBoxLayout, QWidget)
import images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(383, 853)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_login = QFrame(self.centralwidget)
        self.frame_login.setObjectName(u"frame_login")
        self.frame_login.setStyleSheet(u"background-color: rgb(58, 58, 58);")
        self.frame_login.setFrameShape(QFrame.StyledPanel)
        self.frame_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_usuario = QFrame(self.frame_login)
        self.frame_usuario.setObjectName(u"frame_usuario")
        self.frame_usuario.setFrameShape(QFrame.StyledPanel)
        self.frame_usuario.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_usuario)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_usuar = QLabel(self.frame_usuario)
        self.lbl_usuar.setObjectName(u"lbl_usuar")
        self.lbl_usuar.setScaledContents(False)

        self.verticalLayout.addWidget(self.lbl_usuar)

        self.img_label1 = QLabel(self.frame_usuario)
        self.img_label1.setObjectName(u"img_label1")
        self.img_label1.setPixmap(QPixmap(u":/image/fJ4AMqw.png"))
        self.img_label1.setScaledContents(True)

        self.verticalLayout.addWidget(self.img_label1)

        self.input_usu = QLineEdit(self.frame_usuario)
        self.input_usu.setObjectName(u"input_usu")
        self.input_usu.setEchoMode(QLineEdit.Normal)

        self.verticalLayout.addWidget(self.input_usu)


        self.verticalLayout_3.addWidget(self.frame_usuario)

        self.frame_senha = QFrame(self.frame_login)
        self.frame_senha.setObjectName(u"frame_senha")
        self.frame_senha.setFrameShape(QFrame.StyledPanel)
        self.frame_senha.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_senha)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_senha = QLabel(self.frame_senha)
        self.lbl_senha.setObjectName(u"lbl_senha")
        self.lbl_senha.setScaledContents(False)

        self.verticalLayout_2.addWidget(self.lbl_senha)

        self.label = QLabel(self.frame_senha)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/image/fJ4AMqw.png"))
        self.label.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.label)

        self.input_senha = QLineEdit(self.frame_senha)
        self.input_senha.setObjectName(u"input_senha")
        self.input_senha.setEchoMode(QLineEdit.Password)

        self.verticalLayout_2.addWidget(self.input_senha)


        self.verticalLayout_3.addWidget(self.frame_senha)


        self.verticalLayout_4.addWidget(self.frame_login)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lbl_usuar.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Usu\u00e1rio</span></p></body></html>", None))
        self.img_label1.setText("")
        self.input_usu.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu login", None))
        self.lbl_senha.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:18pt;\">Senha</span></p></body></html>", None))
        self.label.setText("")
        self.input_senha.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
    # retranslateUi
