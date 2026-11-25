with open("programming.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Este conteúdo substituiu o anterior.\\n")
print(Path("programming.txt").read_text(encoding="utf-8"))