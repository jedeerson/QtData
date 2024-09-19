
import sqlite3

class sqlite_db:

    def __init__(self,banco =None): #Cria banco de dados
        self.conn = None
        self.cursor = None

        if banco:
            self.open(banco)



    def open(self,banco): #Executado com sucesso
        try:
            self.conn = sqlite3.connect(banco)
            self.cursor = self.conn.cursor()
            print("Conexão criada com sucesso!")
        except sqlite3.Error as e:
            print("Não foi possivel estabelecer conexão!")


    def criar_tabelas(self): #Criar tabelas
        cur = self.cursor
        cur.execute("""CREATE TABLE servicos(
            ID integer primary key autoincrement,
            Nome text NOT NULL,
            Preço numeric NOT NULL,
            Observação text NOT NULL)""") 

    def inserir_apagar_atualizar(self,query):
        cur = self.cursor
        cur.execute(query)
        self.conn.commit()

    def pegar_dados(self,query): 
        cur = self.cursor
        cur.execute(query)
        return cur.fetchall()   


# db = sqlite_db("servicos.db")  #Criando nome das tabelas

# db.inserir_apagar_atualizar("INSERT INTO colaboradores (Nome,CPF,Nascimento,Setor,CEP,Endereço,Login,Senha,Acesso) VALUES ('Jederson Remoeri', '09633195900', '22/06/1996', 'adm', '81925450', 'Desembargador Carlos Pinheiro Guimaraes', 'jeder', 'paocomovo', 'admin')")

# db.inserir_apagar_atualizar("UPDATE colaboradores SET Admin='1' WHERE Admin='0' ")

# db.criar_tabelas() #Criando tabelas