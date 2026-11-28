import sqlite3

def insertDB(linha):
    campos = linha.split("###")  # Divide a linha em campos usando "###" como separador.
    banco.execute("""
        INSERT INTO livros VALUES (?,?,?,?,?)""",
        (campos[0], campos[1], campos[2], campos[3], campos[4]))  # Insere os valores na tabela `livros`.

conn = sqlite3.connect('livraria.db')  # Conecta ao banco existente 'livraria.db'.
banco = conn.cursor()  # Cria um cursor para executar comandos SQL.

with open('create.sql') as file_object:
    conteudo = file_object.readlines()  # Lê todas as linhas do arquivo `create.sql`.

for line in conteudo:
    insertDB(line)  # Insere cada linha de dados na tabela.

conn.commit()  # Salva as alterações no banco.
conn.close()  # Fecha a conexão com o banco de dados.