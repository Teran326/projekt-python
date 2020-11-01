def calc(prvni, druhy, operand):
    print("Vas vysledek:")
    if operand == 1:
        print(prvni + druhy)
    elif operand == 2:
        print(prvni - druhy)
    elif operand == 3:
        print(prvni * druhy)
    else:
        print(prvni / druhy)
    return

def pretypovani(a):
    zmena = int(a)
    return zmena

hodnotaA = input("Zadejte prvni hodnotu: ")
hodnotaA = pretypovani(hodnotaA)
hodnotaB = input("Zadejte druhou hodnotu: ")
hodnotaB = pretypovani(hodnotaB)
operace = input("Zadejte operaci pro vypocet vysledku, 1 - soucet, 2 - rozdil, 3 - soucin, 4 - podil: ")
operace = pretypovani(operace)
if operace >= 1 and operace <= 4:
    calc(hodnotaA, hodnotaB, operace)
else:
    print("Zadal jste spatne cislo")