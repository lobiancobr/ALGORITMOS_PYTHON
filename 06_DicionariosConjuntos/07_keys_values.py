# PY06 - Percorrendo chaves e valores de um dicionário (.keys / .values)
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for chave in favorite_languages.keys():
    print(chave.title())

print('=' * 30)

for valores in favorite_languages.values():
    print(valores.title())