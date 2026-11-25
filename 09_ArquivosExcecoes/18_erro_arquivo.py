# Execute para observar FileNotFoundError
with open("arquivo_que_nao_existe.txt", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()