import json

numeros = [2, 3, 5, 7, 11, 13]
with open("numbers.json", "w", encoding="utf-8") as arquivo:
    json.dump(numeros, arquivo)

with open("numbers.json", encoding="utf-8") as arquivo:
    numeros_lidos = json.load(arquivo)

print(numeros_lidos)
print("Tipo:", type(numeros_lidos))