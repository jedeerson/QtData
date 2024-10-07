from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar interface e banco de dados
from templates.cadastrar_servicos import Ui_cadastrar_servicos
from db.query import sqlite_db


# Executavel e botões
class cadastrarservicos(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarservicos,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_servicos()
        self.ui.setupUi(self)
        self.ui.btn_Cadastro_Servico.clicked.connect(self.add)
        self.ui.btn_Cancelar_Servico.clicked.connect(self.can)
        self.ui.btn_Limpar_Usuario.clicked.connect(self.limpar)
        self.ui.btn_pesquisar_servicos.clicked.connect(self.pesquisar)
        self.ui.btn_excluir_servicos.clicked.connect(self.excluir_servicos)
        self.ui.refresh.mousePressEvent = self.on_refresh_click
        self.carregadados_servicos()


# Botão de adicionar dados no banco
    def add(self):
        db = sqlite_db("servicos.db")

        name = self.ui.Nome_Servico.text()
        preco = self.ui.Preco_Servico.text()
        obs = self.ui.OBS_Servico.text()

        if name == "" or preco =="" or obs =="":
            QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!") 
        else:
            db.inserir_apagar_atualizar("INSERT INTO servicos (Nome, Preço, Observação) VALUES ('{}', '{}', '{}') ".format(name,preco,obs)) 
            QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


# Botão de cancelar
    def can(self):
        self.close()


# Botão de limpar
    def limpar(self):
        self.ui.Nome_Servico.setText("")
        self.ui.Preco_Servico.setText("")
        self.ui.OBS_Servico.setText("")    


# Botão de atualizar
    def on_refresh_click(self, event):
        if event.button() == Qt.LeftButton:
            self.carregadados_servicos()


# Botão de pesquisar 
    def pesquisar(self):
        db = sqlite_db("servicos.db")
        valor_consulta =""
        valor_consulta = self.ui.line_pesquisar_servicos.text()

        lista = db.pegar_dados(f"SELECT * FROM servicos where Nome like '%{valor_consulta}%' or Preço like'%{valor_consulta}%' or Observação like'%{valor_consulta}%'")
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
    def excluir_servicos(self):
        try:
            db = sqlite_db("servicos.db")
            id = self.pegar_dados_da_tabela()
            print(id)
            db.inserir_apagar_atualizar("DELETE FROM servicos WHERE id='{}'".format(id))
            QMessageBox.information(QMessageBox(), "AVISO!", f"Dados excluídos!")
            self.carregadados_servicos()
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
    def carregadados_servicos(self):
            db = sqlite_db("servicos.db")
            lista = db.pegar_dados("SELECT * FROM servicos")
            lista.reverse()
            
            self.ui.tableWidget.setRowCount(0)
            for linha, dados in enumerate(lista):
                self.ui.tableWidget.insertRow(linha)
                for coluna_servicos, dados in enumerate(dados):
                    self.ui.tableWidget.setItem(linha,coluna_servicos,QTableWidgetItem(str(dados)))                           


