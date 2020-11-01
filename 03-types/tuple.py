'''
Tuples - neměnitelné n-tice hodnot (seřazený seznam prvků)
V pythonu se n_tice zapisují do kulatých závorek ().
'''

# Vytvoření tuples
numbers = (1, 2, 3)
print('numbers: ', numbers)
print('Type(numbers): ',type(numbers))

chars = tuple('Hello world')
print('chars: ', chars)
print('Type(chars): ',type(chars))

# K vytvoření tuple pouze s jedním prvkem, musí se na konec prvku přidat čárka ('prvek',), jinak to python nevyhodnotí jako tuple.
colors = ('red',)
print('colors: ', colors)

# Součet tuples
print(f'chars + numbers: {chars + numbers}')

# Výpis hodnot 
# Lze specifikovat rozmezí indexů specifikováním začátku a konce rozmezí.
# Při specfikování rozmezí, návratová hodnota bude nový tuple se specifikovanýmy prvky.
print(f'chars[2:5]: {chars[2:5]}')

# Záporné indexování znamená počátek na konci, -1 odkazuje na poslední prvek, -2 odkazuje na předposlední atd.
# Specifikujte negativní indexy pokud chcete začít hledat od konce n_tice:
# Tento příklad vrací hodnotu z indexu -4 (zahrnuto) do indexu -1 (vyloučeno)
print(f'chars[-4:-1]: {chars[-4:-1]}')

# Pro zjištění kolik prvků má n_tice používáme metodu len():
print(f'len(chars): {len(chars)}')

# Zjištění prvního výskytu a počtu výskytu prvku
if 'l' in chars:
    print(f'chars.index("l"): {chars.index("l")}')
    print(f'chars.count("l"): {chars.count("l")}')

# Záměna hodnot proměnných
x = 10
y = 2
x, y = y, x
print(f'x: {x}, y: {y}')
