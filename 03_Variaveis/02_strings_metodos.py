# PY03 - Strings: métodos de manipulação
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

message = "Hello, " + full_name.title() + "!"
print(message)

print(full_name.upper())
print(full_name.lower())
print(full_name.title())
print(full_name.capitalize())
print(full_name.title().swapcase())
print(full_name.title().center(40, '*'))
print(full_name.replace(' ', '_'))
print(full_name.split())