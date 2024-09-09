from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


from templates.cadastrar_colaboradores import Ui_cadastrar_colaboradores
from db.query import sqlite_db


class cadastrarcolaboradores(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarcolaboradores,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_colaboradores()
        self.ui.setupUi(self)
        self.ui.btn_cadastro_usuario.clicked.connect(self.add)  
        self.ui.btn_cancelar_usuario.clicked.connect(self.can)
        self.ui.btn_limpar_usuario.clicked.connect(self.limpar)  


    def add(self):
        db = sqlite_db("colaboradores.db")

        name = self.ui.nome_usuario.text()
        numerodocumento = self.ui.cpf_usuario.text()
        datanascimento = self.ui.nascimento_usuario.text()
        nomesetor = self.ui.setor_usuario.text()
        numerocep = self.ui.cep_usuario.text()
        numeroendereco = self.ui.endereo_usuario.text()
        user = self.ui.login_usuario.text()
        password = self.ui.senha_usuario.text()
        admin = 1

        if name == "" or numerodocumento == "" or datanascimento == "" or nomesetor == "" or numerocep == "" or numeroendereco == "":
            QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")
        else:
            db.inserir_apagar_atualizar("INSERT INTO colaboradores (Nome, CPF, Nascimento, Setor, CEP, Endereço, Login, Senha, Acesso) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name,numerodocumento,datanascimento,nomesetor,numerocep,numeroendereco,user,password,admin))
            QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


    def can(self):
        pass


    def limpar(self):
       self.ui.nome_usuario.setText("")
       self.ui.cpf_usuario.setText("")
       self.ui.nascimento_usuario.setText("")
       self.ui.setor_usuario.setText("")
       self.ui.cep_usuario.setText("")
       self.ui.endereo_usuario.setText("")
       self.ui.login_usuario.setText("")
       self.ui.senha_usuario.setText("")
       admin = 1