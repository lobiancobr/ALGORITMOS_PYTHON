filename = "pi_digits.txt"
with open(filename, encoding="utf-8") as file_object:
    contents = file_object.readlines()
for line in contents:
    print(line.rstrip())