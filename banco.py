import sqlite3
from sqlite3 import Error

######### Criando conexão com Banco de dados
def ConexaoBanco():
    caminho = "C:\\Users\\alyss\\Desktop\\bicho-game\\banco_bolao.db"
    con=None
    try:
        con.sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

