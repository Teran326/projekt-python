'''
 Set je množina jedinečných hodnot
 Set je sbírka, která je neúspořádaná a neindexovaná.
 V Pythonu se zapisují do složených závorek.
'''
my_set = {2, 3, 9, 7}
print('Množina my_set: ', my_set)
print('Typ my_set: ', type(my_set))

# Vytvoření množiny ze seznamu hodnot (list)
numbers = [1, 4, 1, 5, 3, 3, 1, 2, 8, 2]
print(f'Proměnná numbers - seznam (list): {numbers}')
set_numbers = set(numbers)
print(f'Proměnná set_numbers - množina (set): {set_numbers}')

# Vytvoření množiny jedinečných znaků z řetězce
chars = sorted(list('Hello world'))
set_chars = set(chars)
print(f'Uspořádaná množina (set) jedinečných hodnot: {set_chars}')

# Jakmile už je jednou vytvořena, nelze měnit hodnoty prvků, ale lze přidat nové prvky.
# K přidání jednoho prvku lze použít metodu add().
set_chars.add('V')

# K přidání více prvků můžeme užít metodu update().
set_chars.update('X', 'Y', 'Z')

# Pro vymazání prvku užíváme metodu remove() nebo discard().
set_chars.remove('H')
print(f'Proměnná set_chars: {set_chars}')

# Metoda clear() vyprázdní množinu (set)
set_chars.clear()

# Klíčové slovo del vymaže množinu (set) úplně:
del set_chars

# Přístup k hodnotám množiny
# Nelze přistupovat k prvkům za pomoci indexu, jelikož množiny (sets) jsou neúspořádané, tudíž nemají žádný index.
# my_set[1]

# Lze k nim ale přistupovat za pomocí cyklu for, nebo zda je specifická hodnota v množině přítomna, za pomocí klíčového slova in.
for x in my_set:
  print(x)

'''
Množinové operace
'''
# Sjednocení množin
print(f'set_numbers | my_set: {set_numbers | my_set}')
print(f'set_numbers.union(my_set): {set_numbers.union(my_set)}')
# Průnik množin
print(f'set_numbers & my_set: {set_numbers & my_set}')
print(f'set_numbers.intersection(my_set): {set_numbers.intersection(my_set)}')
# Rozdíl množin
print(f'set_numbers - my_set: {set_numbers - my_set}')
print(f'set_numbers.difference(my_set): {set_numbers.difference(my_set)}')
# Doplněk množin
print(f'set_numbers ^ my_set: {set_numbers ^ my_set}')
print(f'set_numbers.symmetric_difference(my_set): {set_numbers.symmetric_difference(my_set)}')
# Zjištění zda množina obsahuje hodnotu
print(f'1 in set_numbers: {1 in set_numbers}')
