import sqlite3

conn = sqlite3.connect('livraria.db')  # Conecta ao banco de dados.
banco = conn.cursor()

# Coleta os dados para o novo registro.
print("REGISTRO NOVO")
print(60*'=')
isbn    = input("ISBN:    ")
titulo  = input("Título:  ")
autor   = input("Autor:   ")
paginas = int(input("Páginas: "))
preco   = float(input("Preço:   "))

# Exibe os dados para confirmação antes de inserir.
print(60*'=')
print("ISBN:    "+ isbn)
print("Título:  "+ titulo)
print("Autor:   "+ autor)
print("Páginas: "+ str(paginas))
print("Preço:   "+ f'R$ {preco:.2f}')

print(60*'=')
inserir = input('Digite SIM para inserir: ')  # Solicita confirmação.
if inserir == "SIM":
    banco.execute("""
        INSERT INTO livros VALUES (?,?,?,?,?)""",
    (isbn, titulo, autor, paginas, preco))  # Insere o registro.

conn.commit()  # Salva as alterações no banco de dados.
conn.close()  # Fecha a conexão.