from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.Qt import Qt
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
import os,sys

from templates.cadastrar_fornecedores import Ui_cadastrar_fornecedores

class cadastrarfornecedores(QDialog):
    def __init__(self, *args,**argvs):
        super(cadastrarfornecedores,self).__init__(*args,**argvs)
        self.ui = Ui_cadastrar_fornecedores()
        self.ui.setupUi(self)
