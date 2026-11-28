import sqlite3

conn = sqlite3.connect('livraria.db')  # Conecta ao banco de dados.
banco = conn.cursor()

procura = str(input('Digite o ISBN do registro que deseja apagar: '))  # Recebe o ISBN do usuário.
query = "SELECT * FROM livros WHERE isbn LIKE "+str(procura)  # Busca o registro com o ISBN fornecido.
consulta = banco.execute(query)

# Exibe as informações do registro encontrado.
for linha in consulta.fetchall():
    print(60*'=')
    print("ISBN:    "+ linha[0])
    print("Título:  "+ linha[1])
    print("Autor:   "+ linha[2])
    print("Páginas: "+ str(linha[3]))
    print("Preço:   "+ f'R$ {linha[4]:.2f}')

print(60*'=')
apagar = input('Digite SIM se confirma: ')  # Solicita confirmação para apagar.
if apagar == "SIM":
    query = "DELETE FROM livros WHERE isbn = ?" # Apaga o registro.
    banco.execute(query, (procura,))

conn.commit()  # Salva as alterações.
conn.close()  # Fecha a conexão.