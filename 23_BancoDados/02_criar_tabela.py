import sqlite3

conn = sqlite3.connect('livraria.db')  # Conecta ou cria o banco de dados chamado 'livraria.db'.
banco = conn.cursor()  # Cria um cursor para executar comandos SQL.

banco.execute("""
    CREATE TABLE livros(
    isbn varchar(13),
    titulo varchar(80) NOT NULL,
    autor varchar(80) NOT NULL,
    paginas smallint NOT NULL,
    preco float NOT NULL);
    """)  # Cria a tabela `livros` com colunas para ISBN, título, autor, número de páginas e preço.

print("Banco livraria e tabela criados com sucesso")  # Mensagem de confirmação para o usuário.

conn.commit()  # Salva as alterações no banco.
conn.close()  # Fecha a conexão com o banco de dados.