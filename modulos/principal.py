from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar telas 
from templates.tela_principal import Ui_tela_principal
from modulos.cdt_clientes import cadastrarclientes
from modulos.cdt_colaboradores import cadastrarcolaboradores
from modulos.cdt_produtos import cadastrarprodutos
from modulos.cdt_servicos import cadastrarservicos
from modulos.cdt_fornecedores import cadastrarfornecedores


# Executavel e botões
class telaprincipal(QMainWindow):
	def __init__(self,telalogin,logado,*args,**argvs):
		super(telaprincipal,self).__init__(*args,**argvs)
		self.ui = Ui_tela_principal()
		self.ui.setupUi(self)
		self.telalogin = telalogin
		self.ui.actionPessoas_4.triggered.connect(self.clientes)
		self.ui.actionColaboradores_2.triggered.connect(self.coloboradores)	
		self.ui.actionProdutos_4.triggered.connect(self.produtos)
		self.ui.actionServi_os_6.triggered.connect(self.servicos)
		self.ui.actionFornecedor.triggered.connect(self.fornecedores)
		self.userlogado = logado
		self.ui.logado.setText(self.userlogado)


# Função tela Clientes
	def clientes(self):
		self.window = cadastrarclientes()
		self.window.show()


# Função tela Colaboradores
	def coloboradores(self):
		self.window = cadastrarcolaboradores()
		self.window.show()	


# Função tela Produtos
	def produtos(self):
		self.window = cadastrarprodutos()
		self.window.show()


# Função tela Serviços
	def servicos(self):
		self.window = cadastrarservicos()
		self.window.show()	


# Função tela Fornecedores
	def fornecedores(self):
		self.window = cadastrarfornecedores()
		self.window.show()	


# Função fechar tela para abrir com outro usuário
	def closeEvent(self, event):
			reply = QMessageBox.question(self, 'Alerta!',
										"Tem certeza que deseja sair?", QMessageBox.Yes |
										QMessageBox.No, QMessageBox.No)
			if reply == QMessageBox.Yes:
				event.accept()
				self.telalogin.show()
				self.clearMask()
				self.destroy()
			else:
				event.ignore()