def pocetZnaku(jazykolam):
    pocet = {}
    for i in jazykolam:
        if i in pocet:
            pocet[i] += 1
        else:
            pocet[i] = 1
    print(pocet)
jazykolam = 'Tři sta třicet tři stříbrných stříkaček přestříkalo přes tři sta třicet tři stříbrných střech'
pocetZnaku(jazykolam)