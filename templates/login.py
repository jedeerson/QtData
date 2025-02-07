
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap


class Ui_tela_login(object):
    def setupUi(self, Tela_Login):
        Tela_Login.setObjectName("Tela_Login")
        Tela_Login.resize(407, 577)
        self.Container1 = QtWidgets.QFrame(Tela_Login)
        self.Container1.setEnabled(True)
        self.Container1.setGeometry(QtCore.QRect(10, -1, 391, 491))
        self.Container1.setStyleSheet("border-radius:20px;\n"
"")
        self.Container1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container1.setObjectName("Container1")
        self.txt_ID = QtWidgets.QLineEdit(self.Container1)
        self.txt_ID.setGeometry(QtCore.QRect(150, 289, 131, 25))
        self.txt_ID.setStyleSheet("QLineEdit#txt_ID {\n"
"      border-radius:10px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"\n"
"\n"
"")
        self.txt_ID.setText("")
        self.txt_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_ID.setObjectName("txt_ID")
        self.txt_senha = QtWidgets.QLineEdit(self.Container1)
        self.txt_senha.setGeometry(QtCore.QRect(150, 329, 131, 25))
        self.txt_senha.setStyleSheet("QLineEdit#txt_senha {\n"
"      border-radius:10px;\n"
"    border: 2px solid white;\n"
"}\n"
"\n"
"\n"
"")
        self.txt_senha.setText("")
        self.txt_senha.setEchoMode(QtWidgets.QLineEdit.Password)
        self.txt_senha.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_senha.setObjectName("txt_senha")
        self.Icone_Login = QtWidgets.QLabel(self.Container1)
        self.Icone_Login.setGeometry(QtCore.QRect(89, 271, 61, 41))
        self.Icone_Login.setStyleSheet("image: url(:/Login/Img/Login.png);")
        self.Icone_Login.setText("")
        self.Icone_Login.setObjectName("Icone_Login")
        self.Icone_Senha = QtWidgets.QLabel(self.Container1)
        self.Icone_Senha.setGeometry(QtCore.QRect(89, 320, 61, 41))
        self.Icone_Senha.setStyleSheet("image: url(:/Login/Img/Senha.png);")
        self.Icone_Senha.setText("")
        self.Icone_Senha.setObjectName("Icone_Senha")
        self.Titulo = QtWidgets.QLabel(self.Container1)
        self.Titulo.setGeometry(QtCore.QRect(50, 80, 291, 191))
        self.Titulo.setObjectName("Titulo")
        self.Btn_Entrar = QtWidgets.QPushButton(self.Container1)
        self.Btn_Entrar.setGeometry(QtCore.QRect(100, 380, 81, 31))
        self.Btn_Entrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Entrar.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(216, 216, 216);\n"
"    color: rgb(0, 0, 0);\n"
"    alternate-background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Btn_Entrar.setObjectName("Btn_Entrar")
        self.Btn_Sair = QtWidgets.QPushButton(self.Container1)
        self.Btn_Sair.setGeometry(QtCore.QRect(204, 380, 81, 31))
        self.Btn_Sair.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Btn_Sair.setStyleSheet("QPushButton{\n"
"\n"
"    background-color: rgb(216, 216, 216);\n"
"    color: rgb(0, 0, 0);\n"
"    alternate-background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Btn_Sair.setObjectName("Btn_Sair")
        self.txt_ID.raise_()
        self.txt_senha.raise_()
        self.Icone_Senha.raise_()
        self.Titulo.raise_()
        self.Icone_Login.raise_()
        self.Btn_Entrar.raise_()
        self.Btn_Sair.raise_()
        self.Container2 = QtWidgets.QFrame(Tela_Login)
        self.Container2.setGeometry(QtCore.QRect(-10, -10, 422, 590))
        self.Container2.setStyleSheet("image: url(:/Login/Img/Fundo.png);")
        self.Container2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Container2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Container2.setObjectName("Container2")
        self.Erro_senha = QtWidgets.QLabel(self.Container2)
        self.Erro_senha.setGeometry(QtCore.QRect(20, 560, 131, 20))
        self.Erro_senha.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Erro_senha.setStyleSheet("QLabel{\n"
"\n"
"    color: rgb(0, 0, 0);\n"
"    alternate-background-color: rgb(255, 255, 255);\n"
"    border-radius:10px;\n"
"\n"
"}\n"
"\n"
"QLabel:hover{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(0, 0, 0);\n"
"}\n"
"")
        self.Erro_senha.setObjectName("Erro_senha")
        self.Container2.raise_()
        self.Container1.raise_()

        self.retranslateUi(Tela_Login)
        QtCore.QMetaObject.connectSlotsByName(Tela_Login)

    def retranslateUi(self, Tela_Login):
        _translate = QtCore.QCoreApplication.translate
        Tela_Login.setWindowTitle(_translate("Tela_Login", "Tela Login"))
        self.txt_ID.setPlaceholderText(_translate("Tela_Login", "ID Login"))
        self.txt_senha.setPlaceholderText(_translate("Tela_Login", "Senha"))
        self.Titulo.setToolTip(_translate("Tela_Login", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\"></span></p></body></html>"))
        self.Titulo.setWhatsThis(_translate("Tela_Login", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Login de Usuário</span></p></body></html>"))
        self.Titulo.setText(_translate("Tela_Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt; font-weight:600; color:#ffffff;\">Login de Usuário</span></p></body></html>"))
        self.Btn_Entrar.setText(_translate("Tela_Login", "Entrar"))
        self.Btn_Sair.setText(_translate("Tela_Login", "Sair"))
        self.Erro_senha.setText(_translate("Tela_Login", "<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ffffff;\">Esqueceu a Senha?</span></p></body></html>"))
from icones import icone_login


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tela_Login = QtWidgets.QWidget()
    ui = Ui_tela_login()
    ui.setupUi(Tela_Login)
    Tela_Login.show()
    sys.exit(app.exec_())
