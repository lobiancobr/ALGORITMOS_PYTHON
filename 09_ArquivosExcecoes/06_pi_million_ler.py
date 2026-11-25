filename = "pi_million_digits.txt"
if Path(filename).exists():
    with open(filename, encoding="utf-8") as file_object:
        lines = file_object.readlines()
    pi_string = ""
    for line in lines:
        pi_string += line.strip()
    print("Caracteres lidos:", len(pi_string))
else:
    print("Arquivo não encontrado. Faça o upload de pi_million_digits.txt.")