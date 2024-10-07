from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar interface e banco de dados
from templates.cadastrar_produtos import Ui_cadastrar_produtos
from db.query import sqlite_db


# Executavel e botões
class cadastrarprodutos(QDialog):
	def __init__(self,*args,**argvs):
		super(cadastrarprodutos,self).__init__(*args,**argvs)
		self.ui = Ui_cadastrar_produtos()
		self.ui.setupUi(self)
		self.ui.btn_cadastro_produtos.clicked.connect(self.add)
		self.ui.btn_cancelar_produtos.clicked.connect(self.can)
		self.ui.btn_cancelar_produtos.clicked.connect(self.limpar)
		self.ui.btn_pesquisar_produtos.clicked.connect(self.pesquisar)
		self.ui.btn_excluir_produtos.clicked.connect(self.excluir_produtos)
		self.ui.refresh.mousePressEvent = self.on_refresh_click
		self.carregadados_produtos()


# Botão de adicionar dados no banco
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


# Botão de cancelar
	def can(self):
		self.close()


# Botão de limpar
	def limpar(self):
			self.ui.Nome.setText("")
			self.ui.Preço.setText("")
			self.ui.Observção.setText("")	


# Botão de atualizar
	def on_refresh_click(self, event):	
					if event.button() == Qt.LeftButton:
						self.carregadados_produtos() 



# Botão de pesquisar 
	def pesquisar(self):
		db = sqlite_db("produtos.db")
		valor_consulta =""
		valor_consulta = self.ui.line_pesquisar_produtos.text()

		lista = db.pegar_dados(f"SELECT * FROM produtos where Nome like '%{valor_consulta}%' or Preço like'%{valor_consulta}%' or Observação like'%{valor_consulta}%'")
		lista = list(lista)
		if not lista:
			return  QMessageBox.warning(QMessageBox(),"Atenção!!", "Não encontrado!")
			
		else:   
			self.ui.tableWidget.setRowCount(0)
			for idxLinha, linha in enumerate(lista):
				self.ui.tableWidget.insertRow(idxLinha)
				for idxColuna, coluna in enumerate(linha):
					self.ui.tableWidget.setItem(idxLinha, idxColuna, QTableWidgetItem(str(coluna)))


# Botão de excluir
	def excluir_produtos(self):
			try:
				db = sqlite_db("produtos.db")
				id = self.pegar_dados_da_tabela()
				print(id)
				db.inserir_apagar_atualizar("DELETE FROM produtos WHERE id='{}'".format(id))
				QMessageBox.information(QMessageBox(), "AVISO!", f"Dados excluídos!")
				self.carregadados_produtos()
			except:
				QMessageBox.warning(QMessageBox(), "AVISO", f"Não foi possível excluir dados!")


# Função de pegar dados do banco
	def pegar_dados_do_banco(self):
		return self.ui.tableWidget.currentRow()
	

# Função de pegar dados da tabela
	def pegar_dados_da_tabela(self):
		valor = self.ui.tableWidget.item(self.pegar_dados_do_banco(), 0)
		return valor.text()


# Função mostrar dados na tabela
	def carregadados_produtos(self):
			db = sqlite_db("produtos.db")
			lista = db.pegar_dados("SELECT * FROM produtos")
			lista.reverse()
			
			self.ui.tableWidget.setRowCount(0)
			for linha, dados in enumerate(lista):
				self.ui.tableWidget.insertRow(linha)
				for coluna_produtos, dados in enumerate(dados):
					self.ui.tableWidget.setItem(linha,coluna_produtos,QTableWidgetItem(str(dados)))

					