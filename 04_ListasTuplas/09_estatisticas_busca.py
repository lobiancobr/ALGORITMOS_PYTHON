# PY04 - Estatísticas e busca (min, max, sum, in, index)
# Definindo a lista de dígitos
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Encontrando o valor mínimo na lista digits
min_value = min(digits)
print(f"Valor mínimo na lista: {min_value}")

# Encontrando o valor máximo na lista digits
max_value = max(digits)
print(f"Valor máximo na lista: {max_value}")

# Calculando a soma de todos os valores na lista digits
sum_value = sum(digits)
print(f"Soma de todos os valores na lista: {sum_value}")

# Procurando um elemento específico na lista
elemento_procurado = 5
if elemento_procurado in digits:
    index_elemento = digits.index(elemento_procurado)
    print(f"O elemento {elemento_procurado} está na posição {index_elemento} da lista.")
else:
    print(f"O elemento {elemento_procurado} não está na lista.")