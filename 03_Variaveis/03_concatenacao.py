# PY03 - Concatenação de strings
# --- Parte 1: concatenação com + e str() ---
age = 23
message = "Happy " + str(age) + "rd Birthday!"
print(message)

# --- Parte 2: entrada de dados e três formas de impressão ---
nome = input("Digite o nome do filme:\n")
ano = int(input("Digite o ano de lançamento do filme:\n"))
nota = float(input("Digite a nota do filme:\n"))

print("Dados do Filme")
print("=========================")
# Alternativa 1 - múltiplas impressões
print("Nome do filme:", nome)
print("Ano de lançamento:", ano)
print("Nota do filme:", nota)

print("=========================")
# Alternativa 2 - impressão concatenada
print("Nome do Filme:", nome, "\nAno de Lançamento:", ano, "\nNota do Filme:", nota)

print("=========================")
# Alternativa 3 - impressão formatada (f-string)
print(f"Nome do jogo: {nome}\n"
      f"Ano de lançamento: {ano}\n"
      f"Nota do filme: {nota}\n"
      )