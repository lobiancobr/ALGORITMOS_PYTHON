if Path("pi_million_digits.txt").exists():
    birthday = input("Data de nascimento (somente números): ").strip()
    if not birthday.isdigit():
        print("Digite apenas números.")
    elif birthday in pi_string:
        print("Sua data aparece no arquivo de dígitos de pi!")
    else:
        print("Sua data não aparece no arquivo.")
else:
    print("Faça o upload de pi_million_digits.txt primeiro.")