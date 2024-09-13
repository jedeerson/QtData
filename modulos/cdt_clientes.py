from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from templates.cadastrar_clientes import Ui_cadastrar_clientes
from db.query import sqlite_db

class cadastrarclientes(QDialog):
	def __init__(self,*args,**argvs):
		super(cadastrarclientes,self).__init__(*args,**argvs)
		self.ui = Ui_cadastrar_clientes()
		self.ui.setupUi(self)
		self.ui.btn_Cadastro_Cliente.clicked.connect(self.add)
		self.ui.btn_Cancelar_Cliente.clicked.connect(self.can)
		self.ui.btn_Cadastrar_Cliente.clicked.connect(self.limpa)
		self.carregadados_clientes()

	def add(self):
		db = sqlite_db("clientes.db")

		name = self.ui.Nome_Cliente.text()
		doc = self.ui.CPF_Cliente.text()
		ape = self.ui.Apelido_Ciente.text()
		end = self.ui.Endereo_Cliente.text()
		nas = self.ui.Nascimento.text()
		tel = self.ui.Telefone_Cliente.text()
		ema = self.ui.Email_Cliente.text()


		if name == "" or doc == "" or ape == "" or end == "" or nas == "" or tel == "" or ema == "":
			QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")
		else:
			db.inserir_apagar_atualizar("INSERT INTO clientes (Nome, CPF_CNPJ, Apelido, Endereço, Nascimento, Número, Email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name,doc,ape,end,nas,tel,ema))
			QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


	def can(self):
		self.close()


	def limpa(self):
		self.ui.Nome_Cliente.setText("")
		self.ui.CPF_Cliente.setText("")
		self.ui.Apelido_Ciente.setText("")
		self.ui.Endereo_Cliente.setText("")
		self.ui.Nascimento.setText("")
		self.ui.Telefone_Cliente.setText("")
		self.ui.Email_Cliente.setText("")


	def carregadados_clientes(self):
		db = sqlite_db("clientes.db")
		lista = db.pegar_dados("SELECT * FROM clientes")
		
		self.ui.tableWidget.setRowCount(0)
		for linha, dados in enumerate(lista):
			self.ui.tableWidget.insertRow(linha)
			for coluna_clientes, dados in enumerate(dados):
				self.ui.tableWidget.setItem(linha,coluna_clientes,QTableWidgetItem(str(dados)))