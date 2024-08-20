
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


from templates.login import Ui_tela_login
from modulos.principal import telaprincipal


class login(QDialog):
	def __init__(self,*args,**argvs):
		super(login,self).__init__(*args,**argvs)
		self.ui = Ui_tela_login()
		self.ui.setupUi(self)
		self.ui.Btn_Entrar.clicked.connect(self.login)
		#self.ui.Btn_Sair.clicked.connect(self.login)

	def login(self):
		admin ="admin"
		senha ="admin"

		user = self.ui.txt_ID.text()
		passwd = self.ui.txt_senha.text() 

		if admin == user and passwd ==senha:
			QMessageBox.information(QMessageBox(), "Login Realizado!", "Entrou com sucesso!")
			self.window = telaprincipal()
			self.window.show()
		else:
			QMessageBox.warning(QMessageBox(), "Login Errado!", "Não Entrou com sucesso!")
	
		login.hide(self)





