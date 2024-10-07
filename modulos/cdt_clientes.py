from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QDialog, QMessageBox, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os, sys


# Importar interface e banco de dados
from templates.cadastrar_clientes import Ui_cadastrar_clientes
from db.query import sqlite_db


# Executavel e botões
class cadastrarclientes(QDialog):
    def __init__(self, *args, **argvs):
        super(cadastrarclientes, self).__init__(*args, **argvs)
        self.ui = Ui_cadastrar_clientes()
        self.ui.setupUi(self)
        self.ui.btn_cadastro_cliente.clicked.connect(self.add)
        self.ui.btn_cancelar_cliente.clicked.connect(self.can)
        self.ui.btn_cadastrar_cliente.clicked.connect(self.limpa)
        self.ui.refresh.mousePressEvent = self.on_refresh_click
        self.ui.btn_pesquisar_clientes.clicked.connect(self.pesquisar)
        self.ui.btn_excluir_clientes.clicked.connect(self.excluir_clientes)
        self.carregadados_clientes()


# Botão de adicionar dados no banco
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
            QMessageBox.information(QMessageBox(), "AVISO", f"PREENCHA TODOS OS CAMPOS!")
        else:
            db.inserir_apagar_atualizar("INSERT INTO clientes (Nome, CPF_CNPJ, Apelido, Endereço, Nascimento, Número, Email) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name, doc, ape, end, nas, tel, ema))
            QMessageBox.information(QMessageBox(), "AVISO", f"DADOS GRAVADOS COM SUCESSO!")


# Botão de cancelar
    def can(self):
        self.close()


# Botão de limpar
    def limpa(self):
        self.ui.nome_cliente.setText("")
        self.ui.cpf_cliente.setText("")
        self.ui.apelido_ciente.setText("")
        self.ui.endereco_cliente.setText("")
        self.ui.telefone_cliente.setText("")
        self.ui.email_cliente.setText("")
        self.ui.nascimento.setDate(QDate.currentDate())  


# Botão de atualizar
    def on_refresh_click(self, event):
        if event.button() == Qt.LeftButton:
            self.carregadados_clientes()


# Botão de pesquisar
    def pesquisar(self):
        db = sqlite_db("clientes.db")
        valor_consulta =""
        valor_consulta = self.ui.line_pesquisar_clientes.text()

        lista = db.pegar_dados(f"SELECT * FROM clientes where Nome like '%{valor_consulta}%' or CPF_CNPJ like'%{valor_consulta}%' or Apelido like'%{valor_consulta}%' or Endereço like'%{valor_consulta}%' or Nascimento like'%{valor_consulta}%' or Número like'%{valor_consulta}%' or Email like'%{valor_consulta}%'")
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
    def excluir_clientes(self):
        try:
            db = sqlite_db("clientes.db")
            id = self.pegar_dados_da_tabela()
            db.inserir_apagar_atualizar("DELETE FROM clientes WHERE id='{}'".format(id))
            QMessageBox.information(QMessageBox(), "AVISO!", f"Dados excluídos!")
            self.carregadados_clientes()
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
    def carregadados_clientes(self):
        db = sqlite_db("clientes.db")
        lista = db.pegar_dados("SELECT * FROM clientes")
        lista.reverse()

        self.ui.tableWidget.setRowCount(0)
        for linha, dados in enumerate(lista):
            self.ui.tableWidget.insertRow(linha)
            for coluna_clientes, dados in enumerate(dados):
                self.ui.tableWidget.setItem(linha, coluna_clientes, QTableWidgetItem(str(dados)))