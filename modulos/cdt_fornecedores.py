from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from templates.cadastrar_fornecedores import Ui_cadastrar_fornecedores
from db.query import sqlite_db

class cadastrarfornecedores(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarfornecedores,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_fornecedores()
        self.ui.setupUi(self)
        self.ui.btn_cadastro_fornecedores.clicked.connect(self.add)
        self.ui.btn_cancelar_fornecedores.clicked.connect(self.can)
        self.ui.btn_cadastrar_fornecedor.clicked.connect(self.limpar)
    
    def add(self):
        db = sqlite_db("fornecedores.db")

        name_fantasia = self.ui.nome_fantasia.text() 
        doc = self.ui.cpf_cnpj_fornecedores.text() 
        name_razao_social = self.ui.razao_social.text() 
        end = self.ui.endereco_fornecedores.text() 
        n_inscricao_estadual = self.ui.inscricao_estadual.text() 
        tel = self.ui.telefone_fornecedores.text() 
        email = self.ui.email_fornecedores.text() 
        tipo_fornecedor = self.ui.tipo_de_fornecedores.text()

        if name_fantasia == "" or doc == "" or name_razao_social == "" or end == "" or n_inscricao_estadual == "" or tel == "" or email == "" or tipo_fornecedor == "":
            QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")
        else:
            db.inserir_apagar_atualizar("INSERT INTO fornecedores (Nome_Fantasia, CPF_CNPJ, Razão_Social, Endereço, Inscricao_Estadual, Telefone, Email, Tipo_de_Fornecedor) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name_fantasia,doc,name_razao_social,end,n_inscricao_estadual,tel,email,tipo_fornecedor))    
            QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


    def can(self):
        pass


    def limpar(self):
        self.ui.nome_fantasia.setText("")
        self.ui.cpf_cnpj_fornecedores.setText("") 
        self.ui.razao_social.setText("")
        self.ui.endereco_fornecedores.setText("") 
        self.ui.inscricao_estadual.setText("")
        self.ui.telefone_fornecedores.setText("")
        self.ui.email_fornecedores.setText("")
        self.ui.tipo_de_fornecedores.setText("")
