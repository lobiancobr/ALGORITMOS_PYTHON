import sqlite3

conn = sqlite3.connect('livraria.db')
banco = conn.cursor()

procura = str(input('Digite o conteúdo que deseja encontrar: '))  # Recebe do usuário o termo para busca.
query = "SELECT * FROM livros WHERE titulo LIKE ?"  # Monta a consulta SQL.
listagem = banco.execute(query, ('%' + procura + '%',))  # Executa a consulta no banco de dados.

for linha in listagem.fetchall():
    print(60 * '=')  # Imprime uma linha separadora para cada registro.
    print("ISBN:    " + linha[0])
    print("Título:  " + linha[1])
    print("Autor:   " + linha[2])
    print("Páginas: " + str(linha[3]))
    print("Preço:   " + f'R$ {linha[4]:.2f}')  # Formata o preço como moeda.

conn.commit()
conn.close()