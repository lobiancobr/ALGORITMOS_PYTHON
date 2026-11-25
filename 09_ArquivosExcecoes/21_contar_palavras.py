filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    print(f"Desculpe, o arquivo {filename} não existe.")
else:
    words = contents.split()
    print(f"O arquivo {filename} tem aproximadamente {len(words)} palavras.")