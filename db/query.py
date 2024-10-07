
import sqlite3

class sqlite_db:


#Cria banco de dados
    def __init__(self,banco =None): 
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)


#Executado com sucesso
    def open(self,banco): 
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possivel estabelecer conexão!")


#Criar tabelas
    def criar_tabelas(self): 
        cur = self.cursor
        cur.execute("""CREATE TABLE servicos(
            ID integer primary key autoincrement,
            Nome text NOT NULL,
            Preço numeric NOT NULL,
            Observação text NOT NULL)""") 


#Inserir dados e apagar 
    def inserir_apagar_atualizar(self,query): 
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()


#Pegar dados do Banco
    def pegar_dados(self,query): 
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()   

