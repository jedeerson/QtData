
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar interface e banco de dados
from templates.login import Ui_tela_login
from modulos.principal import telaprincipal
from db.query import sqlite_db


# Executavel e botões
class login(QDialog):
	def __init__(self,*args,**argvs):
		super(login,self).__init__(*args,**argvs)
		self.ui = Ui_tela_login()
		self.ui.setupUi(self)
		self.ui.Btn_Entrar.clicked.connect(self.login)
		self.ui.Btn_Sair.clicked.connect(self.sair)
		
# Botões para abrir a tela principal
	def login(self):
		db = sqlite_db("colaboradores.db")

		Login = self.ui.txt_ID.text()
		Senha = self.ui.txt_senha.text() 
		if Login ==" " or Senha==" ":
			QMessageBox.warning(QMessageBox(), "Alerta!", "Preencha todos os campos!")
		else:
			dados = db.pegar_dados("SELECT Acesso FROM colaboradores WHERE Login = '{}' and Senha ='{}'" .format(Login,Senha))
			if dados:
				QMessageBox.information(QMessageBox(),"Login realizado!", "ENTROU COM SUCESSO!")
				self.logado = Login
				self.window = telaprincipal(self,self.logado)
				self.window.show()
				self.hide()
			else:
				QMessageBox.warning(QMessageBox(), "Login Errado!", "NÃO ENTROU COM SUCESSO!")
		

# Botão sair 
	def sair(self):
		self.close()




