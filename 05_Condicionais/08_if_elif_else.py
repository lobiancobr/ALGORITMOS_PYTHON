# PY05 - Sintaxe if-elif-else (preço de admissão por idade)
age = 12

if age < 4:      # menores que 4
    price = 0
elif age < 18:   # acima de 4 e menores que 18
    price = 5
elif age < 65:   # acima de 18 e menores que 65
    price = 10
else:            # acima de 65
    price = 5

print("Your admission cost is $" + str(price) + ".")
