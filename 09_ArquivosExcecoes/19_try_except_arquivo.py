filename = "arquivo_que_nao_existe.txt"
try:
    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError as erro:
    print(f"Não foi possível encontrar o arquivo: {filename}")
    print("Detalhe técnico:", erro)
else:
    print(contents)	