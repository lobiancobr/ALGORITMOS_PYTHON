perfil = {
    "nome": "Ana",
    "idade": 22,
    "linguagens": ["Python", "JavaScript"],
    "ativo": True
}
with open("perfil.json", "w", encoding="utf-8") as arquivo:
    json.dump(perfil, arquivo, ensure_ascii=False, indent=4)
print(Path("perfil.json").read_text(encoding="utf-8"))