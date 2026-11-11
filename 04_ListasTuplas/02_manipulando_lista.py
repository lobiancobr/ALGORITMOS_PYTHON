# PY04 - Manipulando uma lista (remove, append, insert, pop)
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print('Lista original')
print(motorcycles)

print('\nRemovendo um elemento da lista')
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me.")

print('\nInserindo ao fim da lista')
motorcycles.append('bmw')
print(motorcycles)

print('\nInserindo em qualquer posicao')
motorcycles.insert(1, 'kawasaki')
print(motorcycles)

print('\nRetirando do final da lista')
popped = motorcycles.pop()
print(motorcycles)