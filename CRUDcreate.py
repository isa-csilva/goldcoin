import mysql.connector

from GoldCoinsCadastro import *
from GoldCoinsCadastro import Ui_TelaCadastro

from conexao import *

def recebeNome(self):
    return super().recebeNome()
    print("{}".format(self.nomeUsuario))

#input de dados
#add_nome_completo =
#ddd = int(input('Digite o DDD: ' ))
#telefone = int(input('Digite o telefone: ' ))
#add_email = input(str('Adicione o email: '))

def numConcat(ddd, telefone):
    ddd = str(ddd)
    telefone = str(telefone)

    ddd += telefone
    return int(ddd)

add_telefone = (numConcat(ddd, telefone))

#Create
def cadastrar (add_nome_completo,add_telefone, add_email):
    try:
    comando_create = f"""INSERT INTO cadastros (nome_completo, telefone, email) VALUES ('{add_nome_completo}', '+
    55{add_telefone}', '{add_email}')""" #comando do SQL pra inserir informação no BD
    cursor.execute (comando_create) #cursor vai excutar o comando
    conexao.commit() #quando edita o banco de dados
except mysql.connector.Error as Err:
    if err.errno == 1062:
        print("Telefone já cadastrado, tente novamente!")
    else: raise

cursor.close()
conexao.close()
