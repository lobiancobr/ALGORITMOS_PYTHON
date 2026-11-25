filename = "programming.txt"
with open(filename, "w", encoding="utf-8") as file_object:
    file_object.write("I love programming.\\n")
    file_object.write("Python makes it fun!\\n")
print(Path(filename).read_text(encoding="utf-8"))