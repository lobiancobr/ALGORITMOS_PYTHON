try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
    lista = [1, 2, 3]
    elemento = lista[numero]
except ValueError:
    print("Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Você não pode dividir por zero.")
except IndexError:
    print("O índice fornecido está fora dos limites da lista.")
except Exception as e:
    print(f"Ocorreu uma exceção não esperada: {e}")
else:
    print(f"O resultado da divisão é: {resultado}")