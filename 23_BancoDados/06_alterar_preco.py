import sqlite3

conn = sqlite3.connect('livraria.db')
banco = conn.cursor()

procura = str(input('Digite o ISBN que deseja alterar o preço: '))  # Recebe o ISBN do usuário.
query = "SELECT * FROM livros WHERE isbn LIKE " + str(procura)  # Consulta o registro com o ISBN fornecido.
consulta = banco.execute(query)

for linha in consulta.fetchall():
    print(60 * '=')
    print("ISBN:    " + linha[0])
    print("Título:  " + linha[1])
    print("Autor:   " + linha[2])
    print("Páginas: " + str(linha[3]))
    print("Preço:   " + f'R$ {linha[4]:.2f}')

print(60 * '=')
Npreco = input('Digite o preço novo: ')  # Recebe o novo preço do usuário.
query = "UPDATE livros SET preco = ? WHERE isbn = ?" # Atualiza o preço.
banco.execute(query, (Npreco, procura))

conn.commit()  # Salva as alterações no banco.
conn.close()  # Fecha a conexão.