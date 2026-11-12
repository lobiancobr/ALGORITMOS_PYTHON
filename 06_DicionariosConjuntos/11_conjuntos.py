# PY06 - Conjuntos (sets)
# Criando um conjunto (set) de filmes
filmsSet = {"Inception", "The Shawshank Redemption",
            "The Dark Knight", "Pulp Fiction", "Interstellar"}

# Exibir o tipo da variável filmsSet
print(f"Tipo da variável filmsSet: {type(filmsSet)}")  # <class 'set'>

# 1 - Buscar o tamanho do set (quantidade de elementos únicos)
print(f"1. Tamanho do conjunto: {len(filmsSet)}")

# 2 - True e 1 são considerados o mesmo valor (True == 1 em Python)
exampleSet = {"Inception", True, 1, 8.7}
print(f"2. Conjunto exemplo: {exampleSet}")  # True e 1 serão tratados como um único valor

# 3 - Adicionar itens de outro conjunto usando update()
filmsSet.update(exampleSet)
print(f"3. Conjunto após update(): {filmsSet}")  # Elementos de exampleSet são adicionados a filmsSet

# 4 - Remover um item do conjunto
filmsSet.remove(True)  # Remove True (que é equivalente a 1 no set)
filmsSet.remove(8.7)   # Remove o número 8.7
print(f"4. Conjunto após remoção: {filmsSet}")

# 5 - Verificar se um elemento está presente no conjunto
print("5.", "Pulp Fiction" in filmsSet)  # Retorna True se o filme estiver no conjunto

# 6 - Percorrer os elementos de um conjunto
print("6. Elementos do conjunto:")
for film in filmsSet:
    print(film)

# 7 - Criar a interseção entre dois conjuntos (elementos em comum)
setA = {"Inception", "Interstellar", "Tenet"}
setB = {"Interstellar", "Dunkirk", "Memento"}
intersection = setA.intersection(setB)
print(f"7. Interseção entre setA e setB: {intersection}")  # {'Interstellar'}

# 8 - Criar a união entre dois conjuntos (todos os elementos únicos de ambos)
unionSet = setA.union(setB)
print(f"8. União entre setA e setB: {unionSet}")

# 9 - Criar a diferença entre dois conjuntos (elementos que estão em A mas não em B)
differenceSet = setA.difference(setB)
print(f"9. Elementos que estão em setA mas não em setB: {differenceSet}")

# 10 - Esvaziar completamente um conjunto
filmsSet.clear()
print(f"10. Conjunto após clear(): {filmsSet}")  # Saída: set()