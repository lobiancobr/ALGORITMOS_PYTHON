import json
ARQUIVO_DIARIO = "diario_leitura.json"

def carregar_registros():
    try:
        with open(ARQUIVO_DIARIO, encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("O arquivo JSON está inválido. Começaremos uma lista vazia.")
        return []

def salvar_registros(registros):
    with open(ARQUIVO_DIARIO, "w", encoding="utf-8") as arquivo:
        json.dump(registros, arquivo, ensure_ascii=False, indent=4)

registros = carregar_registros()
titulo = input("Título do livro: ").strip()
comentario = input("O que você achou da leitura? ").strip()

if titulo and comentario:
    registros.append({"titulo": titulo, "comentario": comentario})
    salvar_registros(registros)
    print("Registro salvo!")
else:
    print("Título e comentário não podem ficar vazios.")

print("\\n--- Diário de leitura ---")
for numero, registro in enumerate(registros, start=1):
    print(f"{numero}. {registro['titulo']}: {registro['comentario']}")
print("Total de registros:", len(registros))