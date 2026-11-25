print("Informe dois números para dividir. Digite 'q' para sair.")
while True:
    first_number = input("\\nPrimeiro número: ")
    if first_number.lower() == "q":
        print("Programa encerrado.")
        break
    second_number = input("Segundo número: ")
    try:
        answer = float(first_number) / float(second_number)
    except ZeroDivisionError:
        print("Não é possível dividir por zero!")
    except ValueError:
        print("Digite valores numéricos válidos.")
    else:
        print("Resultado:", answer)