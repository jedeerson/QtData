from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from templates.cadastrar_servicos import Ui_cadastrar_servicos
from db.query import sqlite_db

class cadastrarservicos(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarservicos,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_servicos()
        self.ui.setupUi(self)
        self.ui.btn_Cadastro_Servico.clicked.connect(self.add)
        self.ui.btn_Cancelar_Servico.clicked.connect(self.can)
        self.ui.btn_Limpar_Usuario.clicked.connect(self.limpar)


    def add(self):
        db = sqlite_db("serviços.db")

        name = self.ui.Nome_Servico.text()
        preco = self.ui.Preco_Servico.text()
        obs = self.ui.OBS_Servico.text()

        if name == "" or preco =="" or obs =="":
            QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!") 
        else:
            db.inserir_apagar_atualizar("INSERT INTO serviços (Nome, Preço, Observação) VALUES ('{}', '{}', '{}') ".format(name,preco,obs)) 
            QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


    def can(self):
        pass


    def limpar(self):
        self.ui.Nome_Servico.setText("")
        self.ui.Preco_Servico.setText("")
        self.ui.OBS_Servico.setText("")    


