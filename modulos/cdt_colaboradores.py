from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys


# Importar interface e banco de dados
from templates.cadastrar_colaboradores import Ui_cadastrar_colaboradores
from db.query import sqlite_db


# Executavel e botões
class cadastrarcolaboradores(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarcolaboradores,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_colaboradores()
        self.ui.setupUi(self)
        self.ui.btn_cadastro_usuario.clicked.connect(self.add)  
        self.ui.btn_cancelar_usuario.clicked.connect(self.can)
        self.ui.btn_limpar_usuario.clicked.connect(self.limpar)
        self.ui.btn_pesquisar_colaboradores.clicked.connect(self.pesquisar)
        self.ui.btn_excluir_colaboradores.clicked.connect(self.excluir_colaboradores)
        self.ui.refresh.mousePressEvent = self.on_refresh_click
        self.carregadados_colaboradores() 


# Botão de adicionar dados no banco
    def add(self):
        db = sqlite_db("colaboradores.db")

        name = self.ui.nome_usuario.text()
        numerodocumento = self.ui.cpf_usuario.text()
        datanascimento = self.ui.nascimento_usuario.text()
        nomesetor = self.ui.setor_usuario.text()
        numerocep = self.ui.cep_usuario.text()
        numeroendereco = self.ui.endereo_usuario.text()
        user = self.ui.login_usuario.text()
        password = self.ui.senha_usuario.text()
        admin = 1

        if name == "" or numerodocumento == "" or datanascimento == "" or nomesetor == "" or numerocep == "" or numeroendereco == "":
            QMessageBox.information(QMessageBox(), "AVISO", "PREENCHA TODOS OS CAMPOS!")
        else:
            db.inserir_apagar_atualizar("INSERT INTO colaboradores (Nome, CPF, Nascimento, Setor, CEP, Endereço, Login, Senha, Acesso) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(name,numerodocumento,datanascimento,nomesetor,numerocep,numeroendereco,user,password,admin))
            QMessageBox.information(QMessageBox(), "AVISO", "DADOS GRAVADOS COM SUCESSO!")


# Botão de cancelar
    def can(self):
        self.close()


# Botão de limpar
    def limpar(self):
       self.ui.nome_usuario.setText("")
       self.ui.cpf_usuario.setText("")
       self.ui.nascimento_usuario.setText("")
       self.ui.setor_usuario.setText("")
       self.ui.cep_usuario.setText("")
       self.ui.endereo_usuario.setText("")
       self.ui.login_usuario.setText("")
       self.ui.senha_usuario.setText("")
       admin = 1


# Botão de atualizar
    def on_refresh_click(self, event):	
            if event.button() == Qt.LeftButton:
                self.carregadados_colaboradores()


# Botão de pesquisar
    def pesquisar(self):
        db = sqlite_db("colaboradores.db")
        valor_consulta =""
        valor_consulta = self.ui.line_pesquisar_colaboradores.text()

        lista = db.pegar_dados(f"SELECT * FROM colaboradores where Nome like '%{valor_consulta}%' or CPF like'%{valor_consulta}%' or Nascimento like'%{valor_consulta}%' or Setor like'%{valor_consulta}%' or CEP like'%{valor_consulta}%' or Endereço like'%{valor_consulta}%'")
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
    def excluir_colaboradores(self):
            try:
                db = sqlite_db("colaboradores.db")
                id = self.pegar_dados_da_tabela()
                print(id)
                db.inserir_apagar_atualizar("DELETE FROM colaboradores WHERE id='{}'".format(id))
                QMessageBox.information(QMessageBox(), "AVISO!", f"Dados excluídos!")
                self.carregadados_colaboradores()
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
    def carregadados_colaboradores(self):
            db = sqlite_db("colaboradores.db")
            lista = db.pegar_dados("SELECT * FROM colaboradores")
            lista.reverse()
            
            self.ui.tableWidget.setRowCount(0)
            for linha, dados in enumerate(lista):
                self.ui.tableWidget.insertRow(linha)
                for coluna_colaboradores, dados in enumerate(dados):
                    self.ui.tableWidget.setItem(linha,coluna_colaboradores,QTableWidgetItem(str(dados)))

    	
              

              