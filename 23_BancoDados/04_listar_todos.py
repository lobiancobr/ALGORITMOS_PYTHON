import sqlite3

conn = sqlite3.connect('livraria.db')  # Conecta ao banco de dados 'livraria.db'.
banco = conn.cursor()  # Cria um cursor para executar comandos SQL.

listagem = banco.execute("""
    SELECT * FROM livros
    """)  # Seleciona todos os registros da tabela `livros`.

for linha in listagem.fetchall():
    print(linha)  # Imprime cada linha retornada pela consulta.

conn.commit()  # Salva quaisquer alterações (neste caso, desnecessário, pois a consulta não altera dados).
conn.close()  # Fecha a conexão com o banco de dados.