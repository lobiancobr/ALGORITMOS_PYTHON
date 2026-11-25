def count_words_silently(filename):
    try:
        with open(filename, encoding="utf-8") as arquivo:
            contents = arquivo.read()
    except FileNotFoundError:
        pass  # Não faz nada se o arquivo não existir
    else:
        print(f"{filename}: {len(contents.split())} palavras")

for filename in ["alice.txt", "little_women.txt", "moby_dick.txt"]:
    count_words_silently(filename)