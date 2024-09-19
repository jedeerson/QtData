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
		self.ui.btn_cadastro_cliente.clicked.connect(self.add)
		self.ui.btn_cancelar_cliente.clicked.connect(self.can)
		self.ui.btn_cadastrar_cliente.clicked.connect(self.limpa)
		self.carregadados_clientes()
		self.ui.refresh.mousePressEvent = self.on_refresh_click

	def add(self):
		db = sqlite_db("clientes.db")

		name = self.ui.nome_cliente.text()
		doc = self.ui.cpf_cliente.text()
		ape = self.ui.apelido_ciente.text()
		end = self.ui.endereco_cliente.text()
		nas = self.ui.nascimento.text()
		tel = self.ui.telefone_cliente.text()
		ema = self.ui.email_cliente.text()


		if name == "" or doc == "" or ape == "" or end == "" or nas == "" or tel == "" or ema == "":
			QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")
		else:
			db.inserir_apagar_atualizar("INSERT INTO clientes (Nome, CPF_CNPJ, Apelido, Endereço, Nascimento, Número, Email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name,doc,ape,end,nas,tel,ema))
			QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


	def can(self):
		self.close()


	def limpa(self):
		self.ui.nome_cliente.setText("")
		self.ui.cpf_cliente.setText("")
		self.ui.apelido_ciente.setText("")
		self.ui.endereco_cliente.setText("")
		self.ui.nascimento.setText("")
		self.ui.telefone_cliente.setText("")
		self.ui.email_cliente.setText("")


	def carregadados_clientes(self):
		db = sqlite_db("clientes.db")
		lista = db.pegar_dados("SELECT * FROM clientes")
		
		self.ui.tableWidget_3.setRowCount(0)
		for linha, dados in enumerate(lista):
			self.ui.tableWidget_3.insertRow(linha)
			for coluna_clientes, dados in enumerate(dados):
				self.ui.tableWidget_3.setItem(linha,coluna_clientes,QTableWidgetItem(str(dados)))

	def on_refresh_click(self, event):	
		if event.button() == Qt.LeftButton:
			self.carregadados_clientes()			
				