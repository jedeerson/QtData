from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar interface e banco de dados
from templates.cadastrar_fornecedores import Ui_cadastrar_fornecedores
from db.query import sqlite_db


# Executavel e botões
class cadastrarfornecedores(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarfornecedores,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_fornecedores()
        self.ui.setupUi(self)
        self.ui.btn_cadastro_fornecedores.clicked.connect(self.add)
        self.ui.btn_cancelar_fornecedores.clicked.connect(self.can)
        self.ui.btn_cadastrar_fornecedor.clicked.connect(self.limpar)
        self.ui.btn_pesquisar_fornecedores.clicked.connect(self.pesquisar)
        self.ui.btn_excluir_fornecedores.clicked.connect(self.excluir_fornecedores)
        self.ui.refresh.mousePressEvent = self.on_refresh_click
        self.carregadados_fornecedores()


# Botão de adicionar dados no banco
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


# Botão de cancelar
    def can(self):
        self.close()


# Botão de limpar
    def limpar(self):
        self.ui.nome_fantasia.setText("")
        self.ui.cpf_cnpj_fornecedores.setText("") 
        self.ui.razao_social.setText("")
        self.ui.endereco_fornecedores.setText("") 
        self.ui.inscricao_estadual.setText("")
        self.ui.telefone_fornecedores.setText("")
        self.ui.email_fornecedores.setText("")
        self.ui.tipo_de_fornecedores.setText("")


# Botão de atualizar
    def on_refresh_click(self, event):	
            if event.button() == Qt.LeftButton:
                self.carregadados_fornecedores()     


# Botão de pesquisar
    def pesquisar(self):
        db = sqlite_db("fornecedores.db")
        valor_consulta =""
        valor_consulta = self.ui.line_pesquisar_fornecedores.text()

        lista = db.pegar_dados(f"SELECT * FROM fornecedores where Nome_Fantasia like '%{valor_consulta}%' or CPF_CNPJ like'%{valor_consulta}%' or Razão_Social like'%{valor_consulta}%' or Endereço like'%{valor_consulta}%' or Inscricao_Estadual like'%{valor_consulta}%' or Telefone like'%{valor_consulta}%' or Email like'%{valor_consulta}%' or Tipo_de_Fornecedor like'%{valor_consulta}%'")
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
    def excluir_fornecedores(self):
            try:
                db = sqlite_db("fornecedores.db")
                id = self.pegar_dados_da_tabela()
                print(id)
                db.inserir_apagar_atualizar("DELETE FROM fornecedores WHERE id='{}'".format(id))
                QMessageBox.information(QMessageBox(), "AVISO!", f"Dados excluídos!")
                self.carregadados_fornecedores()
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
    def carregadados_fornecedores(self):
            db = sqlite_db("fornecedores.db")
            lista = db.pegar_dados("SELECT * FROM fornecedores")
            lista.reverse()
            
            self.ui.tableWidget.setRowCount(0)
            for linha, dados in enumerate(lista):
                self.ui.tableWidget.insertRow(linha)
                for coluna_fornecedores, dados in enumerate(dados):
                    self.ui.tableWidget.setItem(linha,coluna_fornecedores,QTableWidgetItem(str(dados)))