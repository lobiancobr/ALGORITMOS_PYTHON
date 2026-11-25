mensagem = "Olá! Que bom ter você de volta."
with open("mensagem.json", "w", encoding="utf-8") as arquivo:
    json.dump(mensagem, arquivo, ensure_ascii=False)
with open("mensagem.json", encoding="utf-8") as arquivo:
    mensagem_lida = json.load(arquivo)
print(mensagem_lida)