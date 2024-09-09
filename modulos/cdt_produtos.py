from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from templates.cadastrar_produtos import Ui_cadastrar_produtos
from db.query import sqlite_db

class cadastrarprodutos(QDialog):
	def __init__(self,*args,**argvs):
		super(cadastrarprodutos,self).__init__(*args,**argvs)
		self.ui = Ui_cadastrar_produtos()
		self.ui.setupUi(self)
		self.ui.btn_cadastro_produtos.clicked.connect(self.add)
		self.ui.btn_cancelar_produtos.clicked.connect(self.can)
		self.ui.btn_cancelar_produtos.clicked.connect(self.limpar)

	def add(self):
		db = sqlite_db("produtos.db")

		name_produto = self.ui.Nome_Produto.text()
		preco = self.ui.Preco_Produto.text()
		observacao = self.ui.Observcao.text()

		if name_produto =="" or preco == "" or observacao =="":
			QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")	
		else:
			db.inserir_apagar_atualizar("INSERT INTO produtos (Nome, Preço, Observação) VALUES ('{}', '{}', '{}') ".format(name_produto,preco,observacao))
			QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


	def can(self):
		pass


	def limpar(self):
		self.ui.Nome.setText("")
		self.ui.Preço.setText("")
		self.ui.Observção.setText("")	